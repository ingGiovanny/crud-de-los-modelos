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