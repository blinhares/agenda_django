from django.urls import path

from contact import views #aqui deve importar as views criadas como mostrada no ponto 9

app_name = 'contact' #aqui é name space do app.

urlpatterns = [
    
    path('search/',views.search, name='search'),
    path('',views.index, name='index'),
    #CRUD
    path('contact/<int:contact_id>/show_details/',views.contact, name='contact'),
    path('contact/create/',views.create, name='create'),
    path('contact/<int:contact_id>/update/',views.update, name='update'),
    path('contact/<int:contact_id>/delete/',views.delete, name='delete'),
    # crear usuario
    path('user/create/',views.register_user, name='register_user'),
    path('user/login/',views.login_view, name='login'),
    path('user/logout/',views.logout_view, name='logout'),
    path('user/update/',views.user_update, name='user_update'),


]