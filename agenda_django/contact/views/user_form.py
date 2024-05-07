from django.shortcuts import render, get_object_or_404, redirect

# Para typagem
from django.http import HttpResponse
from django.http import HttpRequest

#caregadno os models
from contact.models import Contact

#erro http
from django.http import Http404 #type:ignore

# opcao de OR nas pqesquisas
from django.db.models import Q

#Paginator
from django.core.paginator import Paginator
from contact.forms import RegisterForm, RegisterUpdateForm
## enviar msgens    
from django.contrib import messages

#para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django. contrib.auth.decorators import login_required


def register_user(request:HttpRequest) -> HttpResponse:
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request=request,
                  message='Usuario Criado com Sucesso!')
            return redirect('contact:index')
 
    context = {
        'form': form,
        'site_title': 'Register User - ',
    }

    return render(
        request=request,
        context=context,
        template_name='contact/register.html',
        
    )

def login_view(request:HttpRequest) -> HttpResponse:
    
    form = AuthenticationForm(request=request)

    if request.method == 'POST':
        form = AuthenticationForm(
            request=request,
            data=request.POST )
        
        if form.is_valid():
            user = form.get_user()
            #fazendo login
            auth.login(request=request, user=user)
            messages.success(
                request=request,
                message=f'{user} logado com Sucesso!'
            )
            return redirect('contact:index')
        messages.success(
                request=request,
                message='Login Invalido!'
            )

    context = {
        'form': form,
        'site_title': 'Register User - ',
    }
    return render(
        request=request,
        context=context,
        template_name='contact/login.html',
        
    )

@login_required(login_url='contact:login')
def logout_view(request:HttpRequest) -> HttpResponse:
    
    auth.logout(request=request)
    return redirect('contact:login')

@login_required(login_url='contact:login')
def user_update(request:HttpRequest) -> HttpResponse:
    form = RegisterUpdateForm(instance=request.user )

    if request.method == 'POST':
        form = RegisterUpdateForm(
            data=request.POST,
             instance=request.user )
        
        if form.is_valid():
            form.save()
            
            messages.success(
                request=request,
                message=f'Upadete Realizado!'
            )

            return redirect('contact:user_update')
        
        messages.error(
                request=request,
                message='Login Invalido!'
            )

    context = {
        'form': form,
        'site_title': 'Update User - ',
    } 

    return render(
        request=request,
        context=context,
        template_name='contact/user_update.html',
    )
