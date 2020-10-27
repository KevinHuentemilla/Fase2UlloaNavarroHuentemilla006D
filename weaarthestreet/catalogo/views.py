from django.shortcuts import render
from . models import Producto,Marca
from django.views import generic
# Create your views here.

def index(request):
    num_Productos=Producto.object.all().count()
    num_Marca_tipo=Marca.object.all().count()

    return render(
        request,
        'index.html',
        context={'num_productos': num_Productos, 'num_marca': num_Marca_Tipo},
    )
