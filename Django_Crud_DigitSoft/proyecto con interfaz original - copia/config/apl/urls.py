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
    #url de ventas
    path('ventas/listar/', ventasListview.as_view() , name='ventas_listar'),
    path('ventas/crear/', ventasCreateView.as_view(), name='ventas_crear'),
    path('ventas/editar/<int:pk>/', ventasUpdateView.as_view(), name='ventas_editar'),
    path('ventas/eliminar/<int:pk>/', ventasDeleteView.as_view(), name='ventas_eliminar'),
    
    #url de garantias
    path('garantias/listar/', garantiasListview.as_view() , name='garantias_listar'),
    path('garantias/crear/', garantiasCreateView.as_view(), name='garantias_crear'),
    path('garantias/editar/<int:pk>/', garantiasUpdateView.as_view(), name='garantias_editar'),
    path('garantias/eliminar/<int:pk>/', garantiasDeleteView.as_view(), name='garantias_eliminar'),

    #url de productos
    path('productos/listar/', productoListview.as_view() , name='producto_listar'),
    path('productos/crear/', productoCreateView.as_view(), name='producto_crear'),
    path('productos/editar/<int:pk>/', productoUpdateView.as_view(), name='producto_editar'),
    path('productos/eliminar/<int:pk>/', productoDeleteView.as_view(), name='producto_eliminar'),

    #url de marca
    path('marca/listar/', marcaListview.as_view() , name='marca_listar'),
    path('marca/crear/', marcaCreateView.as_view(), name='marca_crear'),
    path('marca/editar/<int:pk>/', marcaUpdateView.as_view(), name='marca_editar'),
    path('marca/eliminar/<int:pk>/', marcaDeleteView.as_view(), name='marca_eliminar'),
]

