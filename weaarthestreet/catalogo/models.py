from django.db import models
from django.urls import reverse  #direcciona a una url de un producto al browser
import uuid  #se utiliza para definir atributos claves o la PK

# Create your models here.

class Genero(models.Model):
        marca = models.CharField(max_length=50, help_text='Ingrese si es para hombre, mujer o unisex')
        
    
        def __str__(self):
	        return self.marca

class Producto(models.Model):
    
	    nombre = models.CharField(max_length=100)
	    precio=models.CharField(max_length=50)
        
	    descripcion = models.TextField(max_length=1000, help_text='Ingrese una descripcion')
	    marca=models.ManyToManyField(Genero)
        
       

	
	    def __str__(self):
		    return self.nombre
    
	    def get_absolute_url(self):
		    """Returns the url to access a detail record for this book."""
		    return reverse('book-detail', args=[str(self.id)])
