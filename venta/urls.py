from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name ='Tienda'),
    path('nosotros', views.nosotros, name ='Nosotros'),
    
    path('administracion', views.ProductoListView.as_view(), name ='Admin'),
    path("producto/<pk>", views.ProductoDetailView.as_view(), name="Producto"),
    path('editar/<int:pk>', views.ProductoUpdateView.as_view(), name='Editar'),
    path('agregar', views.ProductoCreateView.as_view(), name='Agregar'),
    path('eliminar/<pk>', views.ProductoEliminarView.as_view(), name='Eliminar'),    
]