from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name='index'),
        path('ropa_hombre/', views.ropa_hombre, name='ropa_hombre'),
        path('zapatilla_hombre/', views.zapatilla_hombre, name='zapatilla_hombre'),
        path('zapatilla_mujer/', views.zapatilla_mujer, name='zapatilla_mujer'),
        path('accesorios', views.accesorios, name='accesorios'),
        path('gg/<int:pk>', views.ProductoDetalles.as_view(), name='producto-detalles')

]
urlpatterns+=[
    
    path('gg/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('gg/<int:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('gg/<int:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
    
    ]