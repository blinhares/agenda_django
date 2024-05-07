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