from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
#parar criar usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import password_validation
#https://docs.djangoproject.com/en/5.0/topics/forms/
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
class ContactForm(forms.ModelForm):
    # #op03
    # first_name =  forms.CharField(
    #     widget= forms.TextInput(
    #         attrs={
    #             'class':'classe-a classe-b',
    #             'placeholder':'Digite seu nome aqui...'
    #         }
    #     ),
    #     label='Primeiro Nome',
    #     help_text='Aqui voce deve digitar seu primeiro nome',#texto de ajuda deve ser renderizado no html
    # )
    
    # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#styling-widget-instances
    # atualiza widgets
    #opcao 02

    # def __init__(self,*args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({
    #         'class':'classe-a classe-b',
    #         'placeholder':'Digite aqui seu email..'

    #     })


    #deixando o campo de inserir fotos mais bonito
    pictures = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'accept':'image/*'
            }
        )
    )
    class Meta:

        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description', 'category',
            'pictures',
            )
        #limita os tipos de dados
        #cria os widgets
        #opcao 01
        # widgets = {
        #     'first_name' :forms.TextInput(
        #         attrs={ #atributos html
        #             'class':'classe-a classe-b',
        #             'placeholder':'Digite aqui seu nome..'
        #         }
        #     ),
        #     'phone':forms.NumberInput,
        #     'email':forms.EmailInput,
        # }
    def clean(self):
        # cleaned_data = self.cleaned_data #captura dados do form

        # self.add_error(
        #     'first_name', ValidationError(
        #         'Menssagem de erro',
        #         code='invalid'
        #     )
        # )#metodo para geracao de erros
        return super().clean()
    
    ############validando dados
    def clean_first_name(self): #nome padrao que é chamado automaticamente
        first_name = self.cleaned_data.get('first_name')

        #exemplo de validacao
        # if first_name == 'ABC':
        #     raise ValidationError('Esse valor nao é suportado')#exemplo de validacao
        #melhor opcao
        if first_name == 'ABC':
            self.add_error(
            'first_name', ValidationError(
                'Menssagem de erro',
                code='invalid'
            )
            )
        return first_name
    
#criando form para Criar usuario
