from django.forms import *
from .models import *

class AdministradorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Administrador
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre',
                }
            ),
            'descripcion' : Textarea(
               attrs={
                  'placeholder' : 'Ingrese una descripción',
                  'rows': 3,
                  'cols': 40,
                }
            ),
        }
        
        
class Facturacionform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_id_venta'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Facturacion
        fields = '__all__'
        widgets = {
            'fecha_id_venta' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese fecha en formato DD/MM/AAAA',
                }
            ),
            'descripcion_venta' : Textarea(
               attrs={
                  'placeholder' : 'Ingrese una descripción',
                  'rows': 3,
                  'cols': 40,
                }
            ),
        }
        

class ventasform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valor_venta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'cliente_id_cliente': Select(
                attrs={
                    'placeholder': 'Seleccione el cliente',
                    'class': 'form-control',
                }
            ),
            'cantidad_vendidas': Textarea(
                attrs={
                    'placeholder': 'Ingrese la cantidad vendida',
                    'rows': 3,
                    'cols': 4,
                }
            ),
        }


class ventasform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valor_venta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'cliente_id_cliente': Select(
                attrs={
                    'placeholder': 'Seleccione el cliente',
                    'class': 'form-control',
                }
            ),
            'cantidad_vendidas': Textarea(
                attrs={
                    'placeholder': 'Ingrese la cantidad vendida',
                    'rows': 3,
                    'cols': 4,
                }
            ),
        }

class garantiasform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['facturacion_id_recibo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Garantias
        fields = '__all__'
        widgets = {
            'facturacion_id_recibo': TextInput(
                attrs={
                    'placeholder': 'Seleccione el recibo',
                    'class': 'form-control',
                }
            ),
            'cantidad_garantias': Textarea(
                attrs={
                    'placeholder': 'Ingrese la cantidad garantías',
                    'rows': 3,
                    'cols': 4,
                }
            ),
        }

class productoform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo_producto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'modelo_producto': TextInput(
                attrs={
                    'placeholder': 'escriba el modelo',
                    'class': 'form-control',
                }
            ),
            'cantidad_producto': Textarea(
                attrs={
                    'placeholder': 'Ingrese la cantidad producto',
                    'rows': 3,
                    'cols': 4,
                }
            ),
        }

class marcaform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'marca' in self.fields:
            self.fields['marca'].widget.attrs['autofocus'] = True  # Ejemplo con 'marca'

    class Meta:
        model = Marca
        fields = '__all__'
