import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent # aponta para a pasta de onde esta o Django
NUMBER_OF_OBJECTS = 1000 # numero de contatos a ser adicionados

sys.path.append(str(DJANGO_BASE_DIR)) # adiciona a pasta ao Path do sistema
#para utilizar o django sem o comando runserver ha que configurar
#a seguinte variavel do sistema. POde observar isso no manager.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
#corrigir um erro de timezone
settings.USE_TZ = False


#https://docs.djangoproject.com/en/5.0/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
django.setup() 

if __name__ == '__main__':
    
    import faker

    from contact.models import Category, Contact #importa os models contacts e category

    Contact.objects.all().delete() #deleta todos os objetos de contact
    Category.objects.all().delete()

    #configurando faker para linguagem de pt-br
    fake = faker.Faker('pt_BR')

    #As cadegorias devem ser criadas primeiro pois ela é chave extrangeira
    categories = ['Amigos', 'Família', 'Conhecidos']
    #criando categorias
    django_categories = [Category(name=name) for name in categories]
    #salvando categorias
    for category in django_categories:
        category.save()

    django_contacts:list[Contact] = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        #cria os objetos que estao dentro da lista de uma vez so
        Contact.objects.bulk_create(django_contacts) 