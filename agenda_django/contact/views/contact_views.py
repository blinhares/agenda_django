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


# Create your views here.

def index(request:HttpRequest) -> HttpResponse:
    
    contacts = Contact.objects.filter(show=True).\
        order_by('-id')
    
    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }

    return render(
        request=request,
        context=context,
        template_name='contact/index.html',
    )

def contact(request:HttpRequest,contact_id:int) -> HttpResponse:
    
    single_contact = get_object_or_404(Contact,id=contact_id, show=True)

    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - '

    }

    return render(
        request=request,
        context=context,
        template_name='contact/contact.html',
    )

def search(request:HttpRequest,) -> HttpResponse:
    search_value = str(request.GET.get('q')).strip()

    # redirecionando pagina em caso de valor vazio
    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains = search_value) |
            Q(last_name__icontains = search_value)|
            Q(phone__icontains = search_value)|
            Q(email__icontains = search_value)
            ).order_by('-id')
    
    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Seach - ',
        'search_value':search_value,
    }

    return render(
        request=request,
        context=context,
        template_name='contact/index.html',
        
    )

