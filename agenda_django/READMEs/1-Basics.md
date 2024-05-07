# Como Trabalhar com Django

## Atalho

```bash
cd Documentos/Python/projetos_python/estudos/Django/ ;
. venv/bin/activate ; cd Agenda ;  python manage.py runserver
```

## 1-Criar Ambiente Virtual

```bash
python -m venv venv
```

### Instalar Lib

```bash
pip install django
```

### Se estiver usando `VsCode`, instalar extenção

Nome: Django

ID: batisteo.vscode-django

Descrição: Beautiful syntax and scoped snippets for perfectionists with deadlines

Versão: 1.15.0

Editor: Baptiste Darthenay

Link do Marketplace do VS: <https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django>

## 2-Iniciando um Projeto

```bash
django-admin startproject project .
```

### Executando Servidor

```bash
python manage.py runserver
```

## 3-Criando um App

```bash
python manage.py startapp <app_name>
```

### Depois de Criado o App Nao esquecer de colocar o nome do app em `settings.py` do projeto

## 4-Configurando o .GitIgnore

<https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/>

## 5-Criando Pasta base de Templates e Arquivos Estaticos

Cria-se uma pasta no diretorio principal do projeto chamada `'base_templates'`.
Nela ficaram armazenados os templates base no nosso projeto do qual faremos referencia posteriormente, mas pra isso a variavel
`TEMPLATES` deve ser alterada e o campo `DIRS` deve passar a apontar tambem para a referida pasta. desta maneira:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base_templates' 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Dentro dessa pasta inclusive se cria outro de nome `global` como name_space para armazenar arquivos gerais do projeto (globais).

Dentro dessa pasta sera criado `base_templates/global/base.html` com um codigo html básico que servira de base para o arquivo index do nosso app. Como veremos a seguir...

## 6-Criando Pasta Arquivos Estaticos

Cria-se uma pasta onde ficaram os arquivos gerais nescessarios para o funcionamento do projeto
como arquivos css e outros, mas pra isso a variavel
`STATICFILES_DIRS` deve ser criada e o seu valor deve apontar para a referida pasta. desta maneira:

```python
STATICFILES_DIRS = (
   BASE_DIR / 'base_static', 
)
```

Dentro dessa pasta tambem se cria outro de nome `global` como name_space para
armazenar arquivos gerais do projeto (globais).

Dentro dessa pasta se criara o seguinte arquivo : `base_static/global/css/style.css` onde seram cologados nosso codigo css.

## 7-Pasta Template dentro do APP

Por padrao, o Django reconhece a pasta template criada dentro de cada App, os arquivos
dentro dessa pasta sao copiados posteriormente na hora do deploy e para evitar problemas
de conflito entre os nomes dos templates, deve-se criar uma nova pasta dentro dela com o mesmo nome do projeto. Ficando assim:

`<NomeProjeto>\templates\<NomeProjeto>`

Dentro dessa pasta criaremos o arquivo index.html que sera a pagina inical do nosso app.

## 8-Extendendo base_templates/global/base.html para contact/templates/contact/inedex.html  

Para extender a pagina de /global/base.html para /contact/inedex.html deve-se utilizar o codigo html django facilitado pela instalacao do plugin no ponto `1`. O codigo fica desta forma:

```django
{% extends "global/base.html" %}
```

## 9-Configurando View

Dentro do arquivo `views.py` dentro do app, se criara todas as respostas HTTP que redirecionara as paginas para o template correspondente realizando a acao programada para tal. O codigo fica assim:

```python
from django.shortcuts import render

# Para typagem
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def index(request:HttpRequest) -> HttpResponse:
    #codigo a ser executado
    return render(
        request=request,
        template_name='contact/index.html',
        
    )
```

A funcao `render` retonara com a nossa pagina criada `contact/index.html` como resposta a requisicao.

## 10-Configurando URLs do App

Para que a pagina seja vizualizada, o codigo python do Framework deve estar corretamente confugurado com uma `url` e uma `view`. Para tanto, deve-se criar o arquivo `urls.py` dentro da pasta do `app` com o seguinte conteudo:

`urls.py`

```python
from django.urls import path

from . import views #aqui deve importar as views criadas como mostrada no ponto 9

app_name = 'contact' #aqui é name space do app.

urlpatterns = [
    path('',views.index, name='index'),
]
```

## 11-Configurando URLs do Projeto

Url criada dentro do app, agora deve se refeverncia dentro do arquivo `urls.py` do `Projeto`!
O arquivo inicialmente encontra-se desta forma:

```python
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

A variavel `urlpatterns` deve ser alterada adicionando a url desejada. O arquivo passa a ficar desta forma:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')), 
]
#path('', include('contact.urls'))
# o primeiro argumento vazio, indica a home da pagina
# O segundo argumento inclui os arquivos de url criados dentro do app
```

## 12-Rodando o Servidor. Vc sera capaz de ver o site que criamos

## 13 - Carregar Arquivos Estaticos em Paginas HTML

Em `base_templates/global/base.html` o arquivo que estara assim:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Qualquer Coisa - Pagina Base - Global</h1>
</body>
</html>
```

Deve passar a ficar assim:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static "global/css/style.css" %}">
</head>
<body>
    <h1>Qualquer Coisa - Pagina Base - Global</h1>
</body>
</html>
```

## 14 - Editar aquivo Css

Editar o arquivo Css localizado em `base_static/global/css/style.css` desta forma:

```css
body{
    background: red;
}
```

## 15 - Apos isso devera aparecer a pagina comfundo vermelho

## 16 - Criando Super Usuario na Area Adm

Corrigindo Migrates

```bash

python manage.py migrate

```

Criando e modificando a senha de um super usuário Django

```bash

python manage.py createsuperuser
```

## 17 - Criando Model para receber os dados

O model é onde os dados vao ser inseridos no projeto. deve-se criar uma classe model com todos os dados e os dipos de dados desejado. Existe um arquivo `models.py` dentro do app que deve ser utilizado para a criacao. Ao editar o arquivo deve ficar desta maneira:

```python

from django.db import models
#importado adicionalmente
from django.utils import timezone

# Create your models here.
#https://docs.djangoproject.com/en/5.0/topics/db/models/

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    phone = models.CharField( max_length = 50 )
    email = models.EmailField( max_length = 254, blank = True )
    created_date = models.DateTimeField( default = timezone.now ) #configura timezone no settings do projeto
    description = models.TextField(blank = True)

```

Sempre que o model for alterado as migracoes devem ser refeitas para que as mudancas sejam efetivadas. Executam-se os seguintes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 18 - Registrando o Model no ADMIN no projeto

Para que a tabela seja exibida no admin do django ela deve estar registrada no arquivo `admin.py` na pasta do app. O arquivo deve ficar desta forma:

```python
from django.contrib import admin

# Register your models here.
from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
```

Apos isso a tabela ja deve aparecer no Admin.

## 19 - Alterando Model pra correta exibicao

Adiciona-se o metodo `__str__` para que a exibicao da classe seja da forma que desejarmos.

```python
class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    phone = models.CharField( max_length = 50 )
    email = models.EmailField( max_length = 254, blank = True )
    created_date = models.DateTimeField( default = timezone.now ) #configura timezone no settings do projeto
    description = models.TextField(blank = True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
```

## 20 - Alterando Configuracao do `admin.py`

Existem diversas configuracoes interessantes para o model. Abaixo um exemplo delas:

```python
# Register your models here.
#  https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # esta configuracao permite que os dados dentro da tupla sejam exibidos 
    # como colunas dentro da area adminstrativa
    # ID é um dado inserido automaticamente pelo django
    list_display = ('id', 'first_name','last_name', 'phone', 'created_date' ) 
    #para mandar os campos ordenados
    # o campo '-id' significa que deve ordenar por id de maneira decrecente. 

    ordering = ('-id',)
    #para filtrar
    list_filter = ('created_date',)
    #criando campo de buscas
    search_fields = ('id', 'first_name','last_name',)
    # numero de contatos por pagina
    list_per_page = 25
    # numero maximo contatos por pagina quando o botao show all for pressioando
    list_max_show_all = 200
    # permitindo modificar campos por clicks ao clicar
    list_editable =  ['first_name','last_name']
    # cara colocar um link para o objeto inteiro
    list_display_links = ['id', 'phone']
```

Para informacoes mais completas, verificar documentação abaixo:

<https://docs.djangoproject.com/en/5.0/ref/contrib/admin/>

## 21 - O Shell do Django

```bash
manage.py shell

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```

## 22 - Adicionando o variavel `STATIC_ROOTS`

É nescessário criar a variavel `STATIC_ROOTS` em `settings.py` que ira apontar para pasta na qual as os arquivos estaticos serao armazenados. Esta pasta nao existe atualmente mas o framework reunira todos os arquivos estaticos nesta pasta e futuramente usaremos isso para subir os arquivos no servidor.

Ficamos assim:

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
   BASE_DIR / 'base_static', 
)
STATIC_ROOT = BASE_DIR / 'static'
```

## 23 - Adicionando o Locais de Media para campo de Pictures

Para adicionar o campo de imagens, é nescessário criar a variavel `MEDIA_URL` e `MEDIA_ROOT` em `settings.py` que ira apontar para pasta na qual as imagens serao armazenadas, localmente e em faze de producao respectivamente.

Ficamos assim:

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
   BASE_DIR / 'base_static', 
)
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 24 - Coletando os Statics e colocando no .GitIgnore

Na linha de comando faca:

```bash
python manage.py collectstatic
```

Adiciona o caminhos das pastas indicadas ao `.gitignore`.

```text
Agenda/static
Agenda/media
```

## 25 - Adicionando o `Picture` e `Show` nos Campos em Models

Seguindo a edicao do arquivo `model.py` que deve ficar desta maneira:

```python
class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    phone = models.CharField( max_length = 50 )
    email = models.EmailField( max_length = 254, blank = True )
    created_date = models.DateTimeField( default = timezone.now ) #configura timezone no settings do projeto
    description = models.TextField(blank = True)
    show = models.BooleanField(default = True)
    #salvara no diretorio configurado na variavel Media em settigns.py criando uma subpasta
    # picture / ano / mes
    pictures = models.ImageField(blank=True, upload_to='picture/%Y/%M') 

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

# Pendente
# category (foreign key)
# owner (foreign key) AUTOMATICO DO DJANGO

#sempre que mecher no model deve refazer as migracoes com os comandos
# makemigrations e migrate para atualizar o banco de dados
```

Agora as migracoes devem ser refeitas para que as mudancas sejam efetivadas.

```bash
python manage.py makemigrations
python manage.py migrate
```

Pode ser que o sistema peça que vc instale o `pillow`. Se pedir, vc instala.

## 26 - Criar Link Para imagens enviadas

Ao clicar no link das imagens enviadas essas n funcionaram pois nao há uma url configrada para tal. Para configurar editaremos o arquivo `urls.py` do projeto adicionadno as seguintes linhas:

```python
from django.conf.urls.static import static
from django.conf import settings
#a func STATIC retorna uma url para cada media dentro da variavel
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 

```

<https://docs.djangoproject.com/en/5.0/ref/urls/#static>

## 27 - Criando o ForengKey no model

O codigo ficaria assim:

```python
class Category(models.Model):
    name = models.CharField( max_length = 50 )
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    phone = models.CharField( max_length = 50 )
    email = models.EmailField( max_length = 254, blank = True )
    created_date = models.DateTimeField( default = timezone.now ) #configura timezone no settings do projeto
    description = models.TextField(blank = True)
    show = models.BooleanField(default = True)
    #salvara no diretorio configurado na variavel Media em settigns.py criando uma subpasta
    # picture / ano / mes
    pictures = models.ImageField(blank=True, upload_to='picture/%Y/%M') 
    #chave estrangeira
    # on delete 'e o que sera realizado quando a categoria for apagado
    category = models.ForeignKey(Category, 
                                 on_delete = models.SET_NULL,
                                 blank = True,
                                 null = True)
    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
```

Registrar o model em `admin.py` com o seguinte codigo:

```python
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_filter = [ 'name']
    list_display = ['name']
```

Agora as migracoes devem ser refeitas para que as mudancas sejam efetivadas.

```bash
python manage.py makemigrations
python manage.py migrate
```

## 28 - Mudando Informação do Model

Para mudar algumas informacoes do modelo se usa a clasee `Meta` cuja a documentacao encontra-se aqui: <https://docs.djangoproject.com/en/5.0/ref/models/options/>. Para adicionar informacao ao nosso model fazermos da seguinte forma:

```python
class Category(models.Model):
    name = models.CharField( max_length = 50 )

    ##para altera os dados do model
    # https://docs.djangoproject.com/en/5.0/ref/models/options/
    class Meta:
        verbose_name = 'Categoria' #seta o nome padrao no singular
        verbose_name_plural = 'Categories' #seta o nome padroa no plural
    
    def __str__(self) -> str:
        return f'{self.name}'
```

## 29 - Adicionando um `owner` (proprietario)

Adicioar um `owner` a um model é importante para descrever qual usuario tera permicoes para manusear livremente  a tabela criada.

Deve-se importar a classe `User`:

```python
from django.contrib.auth.models import User
```

E adicionar o campo no model

```python
class Contact(models.Model):
    first_name = models.CharField( max_length = 50 )
    last_name = models.CharField( max_length = 50 )
    phone = models.CharField( max_length = 50 )
    email = models.EmailField( max_length = 254, blank = True )
    created_date = models.DateTimeField( default = timezone.now ) #configura timezone no settings do projeto
    description = models.TextField(blank = True)
    show = models.BooleanField(default = True)
    #salvara no diretorio configurado na variavel Media em settigns.py criando uma subpasta
    # picture / ano / mes
    pictures = models.ImageField(blank=True, upload_to='picture/%Y/%M') 
    #chave estrangeira
    # on delete 'e o que sera realizado quando a categoria for apagado
    category = models.ForeignKey(Category, 
                                 on_delete = models.SET_NULL,
                                 blank = True,
                                 null = True)
    
    owner = models.ForeignKey(User, 
                                 on_delete = models.SET_NULL,
                                 blank = True,
                                 null = True)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

 
```

Fazer as Migracoes

## 30 - Criando Banco de Dados Aleatorios com script

O Script estara dentro da pasta utils.

## 31 - Usando Uma local Settings nao monitorada pelo git

A pratica consite em importar para o arquivo original `settings.py` do projeto, um arquivo criado chamado `local_settings.py` contendo todas as confiiguracoes nescessarias para cada etada do desenvolvimento.

Isso fara com que as variaveis contidas no arquivo `local_settings.py` sobrescrevam as variaveis do arquivo original.

o arquivo original `settings.py` devera ter ao fina do seu codigo as seguintes linhas:

```python
try:
    from project.local_settings import *
except ImportError:
    ...
```

Lembrando que este arquivo deve ser ignorado pelo git.

## 32 - Organizando VIEWS

Transformar o arquivo `views.py` em um pacote python. Para isso se cria uma pasta com o nome `views` com o arquivo `__init__.py` e o arquivo `.py` contendo os codigo de nossa view ja criada anteriormente.

Feito isso deve-se alterar o arquivo `urls.py` que antes importava o arquivo `views.py` e agora deve importar o `modulos views` criado. O import deve ficar assim:

```python
from contact import views 
```

O arquivo de `__init__.py` deve ficar desta maneira:

```python
from .contact_views import *
```

<https://docs.python.org/3/tutorial/modules.html>
