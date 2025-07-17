from django.urls import path
from apl.views import *
from apl.views.categoria.views import *

app_name = 'apl'

 # path('categoria/listar2/', lista_categoria, name='categoria_lista2'),
 #
 
urlpatterns = [
    path('base/', base_html, name='base'),
    path('plantilla/', plantilla_html, name='plantilla'),
    path('administrador/listar/', AdministradorListView.as_view() , name='administrador_listar'),
    path('administrador/crear/', AdministradorCreateView.as_view(), name='administrador_crear'),
    path('administrador/editar/<int:pk>/', AdministradorUpdateView.as_view(), name='administrador_editar'),
    path('administrador/eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),
    #url de facturacion
    path('facturacion/listar/', FacturacionListview.as_view() , name='facturacion_listar'),
    path('factuacion/crear/', FacturacionCreateView.as_view(), name='facturacion_crear'),
    path('facturacion/editar/<int:pk>/', FacturacionUpdateView.as_view(), name='facturacion_editar'),
    path('facturacion/eliminar/<int:pk>/', FacturacionDeleteView.as_view(), name='facturacion_eliminar'),

]

