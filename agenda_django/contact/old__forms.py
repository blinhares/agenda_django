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
class RegisterForm(UserCreationForm):
    #tornando os campos do form obrigatorio
    first_name = forms.CharField(
        required=True,
        error_messages={
            'required': 'Mensssagem Personalizada'
        }
        
    )
    last_name = forms.CharField(
        required=True,
        
    )
    email = forms.EmailField(
        required=True
        )
    class Meta:
        model = User
        fields = ( 
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )

    def clean_email(self): #validadno email
        email = self.cleaned_data.get('email')
        #verifica se o email ja existe na base de dados
        if User.objects.filter(email=email).\
            exists():
            self.add_error(
                'email',
                ValidationError(
                    'Email já utilizado. Tente Outro',
                    code= 'invalid'),
                )
            
            
        return email
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
