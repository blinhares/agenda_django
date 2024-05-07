from django.db import models
#importado adicionalmente
from django.utils import timezone
#para criar o owner
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length = 50 )
    class Meta:
        verbose_name = 'Categoria' #seta o nome padrao no singular
        verbose_name_plural = 'Categories' #seta o nome padroa no plural
    
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
    pictures = models.ImageField(blank=True, upload_to='picture/%Y/%M') 
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

