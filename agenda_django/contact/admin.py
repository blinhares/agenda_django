from django.contrib import admin

# Register your models here.
#  https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # esta configuracao permite que os dados dentro da tupla sejam exibidos 
    # como colunas dentro da area adminstrativa
    # ID é um dado inserido automaticamente pelo django
    list_display = ('id', 'show' ,'first_name','last_name', 'phone', 'created_date' ) 
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
    list_editable =  ['last_name', 'show']
    # cara colocar um link para o objeto inteiro
    list_display_links = ['id', 'phone']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_filter = [ 'name']
    list_display = ['name']