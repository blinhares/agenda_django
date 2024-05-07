from django.shortcuts import render, \
    get_object_or_404,\
    redirect

# Para typagem
from django.http import HttpResponse
from django.http import HttpRequest

#erro http
from django.http import Http404 #type:ignore

# opcao de OR nas pqesquisas
from django.db.models import Q #type:ignore

from contact.forms import ContactForm

from django.urls import reverse

from contact.models import Contact
from django. contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request:HttpRequest) -> HttpResponse:
    #criando uma variavel que vem do html
    #o comando busca a url do esdereco especifico
    form_action = reverse('contact:create')
    # print('------------')
    # print(form_action)
    # print('------------')
    
    if request.method == 'POST':
        
        form = ContactForm(data=request.POST,
                            files=request.FILES)

        context = {
            'form':form,
            'form_action' :form_action
        }

        if form.is_valid():
            #formulario valido

            contact = form.save(commit=False)
            #adicionando owner a informacao
            contact.owner = request.user

            contact.save()
            # #caso queira mudar algo no formulario enviado antes de 
            # #enviar
            # contact =  form.save(commit=False)
            # contact.show = False
            # contact.save()

            return redirect(
                'contact:update',
                contact_id=contact.id
                )
            

    context = {
        'form': ContactForm(),
        'form_action' :form_action

    }

    return render(
        request=request,
        context= context,
        template_name='contact/create.html',
        
    )

@login_required(login_url='contact:login')
def update(
        request:HttpRequest,
        contact_id:int) -> HttpResponse:
    
    #recebendo obejto pelo ID recebido
    contact = get_object_or_404(
        Contact, 
        id=contact_id, 
        show=True,
        owner=request.user)
    
    form_action = reverse(
        'contact:update',
        args=(contact_id,) 
                           )
   
    
    if request.method == 'POST':
        #formulario com o contato enviado
        form = ContactForm(
            data=request.POST,
            instance=contact,
            files=request.FILES
                           )

        context = {
            'form':form,
            'form_action' :form_action
        }

        if form.is_valid():
            #formulario valido

            contact = form.save()
            # #caso queira mudar algo no formulario enviado antes de 
            # #enviar
            # contact =  form.save(commit=False)
            # contact.show = False
            # contact.save()

            return redirect(
                'contact:update',
                contact_id=contact.id)
            

    context = {
        'form': ContactForm(instance=contact),
        'form_action' :form_action

    }

    return render(
        request=request,
        context= context,
        template_name='contact/create.html',
        
    )

@login_required(login_url='contact:login')
def delete(request:HttpRequest,
           contact_id:int) -> HttpResponse:
    
    #recebendo obejto pelo ID recebido
    single_contact = get_object_or_404(
        Contact, 
        id=contact_id, 
        show=True,
        owner=request.user)
    #coletando confirmacao
    confirmation = request.\
        POST.\
        get('confirmation', 'no')
    #o botao de confirmacao tem um iput hiden
    #  no formulario
    if confirmation == 'yes':
        
        single_contact.delete()
        return redirect('contact:index')

    context = {
        'contact': single_contact,
        'confirmation':confirmation,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - '

    }
    
    

    return render(
        request=request,
        context= context,
        template_name='contact/contact.html',
        
    )