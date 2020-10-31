from django.shortcuts import render
from .models import Producto, Marca
from django.views import generic
# Create your views here.

def index(request):
    
    num_Marca_tipo=Marca.objects.all().count()
    num_Productos=Producto.objects.all().count()
    

    return render(
        request,
        'index.html',
        context={'num_productos': num_Productos, 'num_marca': num_Marca_tipo},
    )


    
