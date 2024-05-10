from django.shortcuts import render
from .models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

def tienda(request):
    producto = Producto.objects.all()
    data = {
        'producto':producto
    }
    return render(request, 'venta/tienda.html', data)

def nosotros(request):
    return render(request, 'venta/nosotros.html')

class ProductoListView(ListView):
    model = Producto
    template_name = 'venta/admin.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'venta/producto.html'

class ProductoCreateView(CreateView):
    model = Producto
    success_url = '/'
    fields = '__all__'
    template_name = 'venta/nuevo_producto.html'
        
class ProductoUpdateView(UpdateView):
    model = Producto
    success_url = '/administracion'
    fields = '__all__'
    template_name = 'venta/editar.html'
    
class ProductoEliminarView(DeleteView):
    model = Producto
    template_name = 'venta/eliminar.html'
    success_url = '/administracion'