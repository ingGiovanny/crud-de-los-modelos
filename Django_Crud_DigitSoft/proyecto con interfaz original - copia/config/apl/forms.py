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
<<<<<<< HEAD
        self.fields['nombre'].widget.attrs['autofocus'] = True
=======
        self.fields['fecha_id_venta'].widget.attrs['autofocus'] = True
>>>>>>> bc407992fb409d052f301d20c2a894c7e58bb89e
        
    class Meta:
        model = Facturacion
        fields = '__all__'
        widgets = {
<<<<<<< HEAD
            'nombre' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre',
                }
            ),
            'descripcion' : Textarea(
=======
            'fecha_id_venta' : TextInput(
                attrs={
                    'placeholder' : 'Ingrese fecha en formato DD/MM/AAAA',
                }
            ),
            'descripcion_venta' : Textarea(
>>>>>>> bc407992fb409d052f301d20c2a894c7e58bb89e
               attrs={
                  'placeholder' : 'Ingrese una descripción',
                  'rows': 3,
                  'cols': 40,
                }
            ),
        }