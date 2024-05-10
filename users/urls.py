from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name ='Login'),
    path('Registro/', views.register, name ='Registro'),
    path('logout/', LogoutView.as_view(template_name='venta/nosotros.html'), name='Logout'),
    
]