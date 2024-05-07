from django.contrib import admin

from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'show' ,'first_name','last_name', 'phone', 'created_date' ) 
    ordering = ('-id',)
    list_filter = ('created_date',)
    search_fields = ('id', 'first_name','last_name',)
    list_per_page = 25
    list_max_show_all = 200
    list_editable =  ['last_name', 'show']
    list_display_links = ['id', 'phone']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_filter = [ 'name']
    list_display = ['name']