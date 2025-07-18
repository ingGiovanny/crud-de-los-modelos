from django import forms
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apl.views.categoria.views import *
#from apl.models import Categoria
from apl.forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required
from apl.models import *

def base_html(request):
    data = {
        'title': 'Base Template',
        'message': 'Welcome to the base template of the application.'
    }
    return render(request, 'categoria/content.html', data)

def plantilla_html(request):
    data = {
        'title': 'Plantilla HTML',
        'message': 'This is a sample HTML template.'
    }
    return render(request, 'categoria/plantilla.html', data)

# a qui estan todas las vistas que hacen que el modulo de asdministradores funcione
# las vistas son las que se encargan de manejar las peticiones y respuestas del usuario
class AdministradorListView(ListView):
    model = Administrador
    template_name = 'administrador/listar_administrador.html'
    context_object_name = 'administradores'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'giovanny'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Administradores'
        context['crear_ruta_url'] = reverse_lazy('apl:administrador_crear')
        context['entidad'] = 'administrador'
        context['administradores'] = Administrador.objects.all()
        return context

class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Administrador'
        return context
    
class AdministradorUpdateView(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Administrador'
        context['entidad'] = 'administradores'
        context['listar_url'] = reverse_lazy('apl:administrador_listar')
        return context
    
class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:administrador_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Administrador'
        context['entidad'] = 'administradores'
        context['listar_url'] = reverse_lazy('apl:administrador_listar')
        return context
#------------------------------------------------------------------------------------------------------------
#a qui van las vistas de facturacion

class FacturacionListview(ListView):
    model = Facturacion
    template_name = 'facturacion/listar_facturacion.html'
    context_object_name = 'facturaciones'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'giovanny'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Facturaciones'
        context['crear_ruta_url'] = reverse_lazy('apl:facturacion_crear')
        context['entidad'] = 'facturacion'
        context['facturacion'] = Facturacion.objects.all()
        return context

class FacturacionCreateView(CreateView):
    model = Facturacion
    form_class = Facturacionform
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear facturacion'
        return context
    
class FacturacionUpdateView(UpdateView):
    model = Facturacion
    form_class = Facturacionform
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar facturacion'
        context['entidad'] = 'facturaciones'
        context['listar_url'] = reverse_lazy('apl:facturacion_listar')
        return context

class FacturacionDeleteView(DeleteView):
    model = Facturacion
    template_name = 'facturacion/eliminar.html'
    success_url = reverse_lazy('apl:facturacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar facturacion'
        context['entidad'] = 'facturaciones'
        context['listar_url'] = reverse_lazy('apl:facturacion_listar')
        return context    
    # ------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
# a qui estan las vistas de ventas



class ventasListview(ListView):
    model = Ventas
    template_name = 'ventas/listar_ventas.html'
    context_object_name = 'ventas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'giovanny'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Ventas'
        context['crear_ruta_url'] = reverse_lazy('apl:ventas_crear')
        context['entidad'] = 'ventas'
        context['ventas'] = Ventas.objects.all()
        return context
    
class ventasCreateView(CreateView):
    model = Ventas
    form_class = ventasform
    template_name = 'ventas/crear.html'
    success_url = reverse_lazy('apl:ventas_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear ventas'
        return context
    
class ventasUpdateView(UpdateView):
    model = Ventas
    form_class = ventasform
    template_name = 'ventas/crear.html'
    success_url = reverse_lazy('apl:ventas_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar ventas'
        context['entidad'] = 'ventas'
        context['listar_url'] = reverse_lazy('apl:ventas_listar')
        return context
    
class ventasDeleteView(DeleteView):
    model = Ventas
    template_name = 'ventas/eliminar.html'
    success_url = reverse_lazy('apl:ventas_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar ventas'
        context['entidad'] = 'ventas'
        context['listar_url'] = reverse_lazy('apl:ventas_listar')
        return context   

#--------------------------------------------------------------------------------------------------------------
#aqui estan las vistas de garantia

class garantiasListview(ListView):
    model = Garantias
    template_name = 'garantia/listar_garantia.html'
    context_object_name = 'garantias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Garantías'
        context['crear_ruta_url'] = reverse_lazy('apl:garantia_crear')
        context['entidad'] = 'garantías'
        context['garantias'] = Garantias.objects.all()
        return context
    
class garantiasCreateView(CreateView):
    model = Garantias
    form_class = garantiasform
    template_name = 'garantia/crear.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear garantías'
        return context
    
class garantiasUpdateView(UpdateView):
    model = Garantias
    form_class = garantiasform
    template_name = 'garantia/crear.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar garantías'
        context['entidad'] = 'garantías'
        context['listar_url'] = reverse_lazy('apl:garantia_listar')
        return context    
    
class garantiasDeleteView(DeleteView):
    model = Garantias
    template_name = 'garantia/eliminar.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar garantías'
        context['entidad'] = 'garantías'
        context['listar_url'] = reverse_lazy('apl:garantia_listar')
        return context
    
#--------------------------------------------------------------------------------------------------------------    
# aqui estan las vistas de productos

class productoListview(ListView):
    model = Producto
    template_name = 'producto/listar_productos.html'
    context_object_name = 'producto'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Producto'
        context['crear_ruta_url'] = reverse_lazy('apl:producto_crear')
        context['entidad'] = 'producto'
        context['producto'] = Producto.objects.all()
        return context
    
class productoCreateView(CreateView):
    model = Producto
    form_class = productoform
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear producto'
        return context

class productoUpdateView(UpdateView):
    model = Producto
    form_class = productoform
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar producto'
        context['entidad'] = 'producto'
        context['listar_url'] = reverse_lazy('apl:producto_listar')
        return context

class productoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/eliminar.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar producto'
        context['entidad'] = 'producto'
        context['listar_url'] = reverse_lazy('apl:producto_listar')
        return context
    
#--------------------------------------------------------------------------------------------------------------    
# aqui estan las vistas de marca

class marcaListview(ListView):
    model = Marca
    template_name = 'marca/listar_marca.html'
    context_object_name = 'marcas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de marcas'
        context['crear_ruta_url'] = reverse_lazy('apl:marca_crear')
        context['entidad'] = 'marcas'
        context['marcas'] = Marca.objects.all()
        return context
    
class marcaCreateView(CreateView):
    model = Marca
    form_class = marcaform
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear marcas'
        return context

class marcaUpdateView(UpdateView):
    model = Marca
    form_class = marcaform
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar marcas'
        context['entidad'] = 'marcas'
        context['listar_url'] = reverse_lazy('apl:marca_listar')
        return context

class marcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/eliminar.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar marcas'
        context['entidad'] = 'marcas'
        context['listar_url'] = reverse_lazy('apl:marca_listar')
        return context