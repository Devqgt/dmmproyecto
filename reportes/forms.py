from .models import ReporteGrupos
from django import forms
from django.forms.fields import DateField
class DateInput(forms.DateInput): 
    input_type = 'date', 

class EjeForm(forms.ModelForm):
    class Meta:
        model = Eje
        fields = [
            'eje_trabajo',
            ]
        labels = { 
            'eje_trabajo':'Eje de trabajo',
            }
        idgets = {
            'eje_trabajo':forms.TextInput(attrs={'class': 'form-control '}), 
             }

class ReporteGruposForm(forms.ModelForm):
    class Meta:
        model = ReporteGrupos
        fields = [
            'eje_trabajo',
            'grupo',
            'nombre_proyecto',
            'descripcion',
            'resultado',
            'beneficiados',
            'presupuesto', 
            'fecha_inicio',
            'fecha_finalizacion', 
            'user',
            ]
        labels = {
            'eje_trabajo':'Eje de trabajo',
            'grupo':'Grupo',
            'nombre_proyecto':'Nombre del proyecto',
            'descripcion':'Descripcion',
            'resultado':'Resultado',
            'beneficiados':'No. Beneficiados',
            'presupuesto':'Presupuesto', 
            'fecha_inicio':'Fecha de inicio',
            'fecha_finalizacion':'Fecha de finalizacion', 
            'user':' Usuario asignado',

        }

        widgets = {
            'eje_trabajo':forms.Select(attrs={'class': 'form-control'}),
            'grupo':forms.TextInput(attrs={'class': 'form-control '}), 
            'nombre_proyecto':forms.TextInput(attrs={'class': 'form-control '}), 
            'descripcion':forms.TextInput(attrs={'class': 'form-control '}), 
            'resultado':forms.TextInput(attrs={'class': 'form-control '}), 
            'beneficiados':forms.TextInput(attrs={'class': 'form-control '}), 
            'presupuesto':forms.TextInput(attrs={'class': 'form-control '}), 
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'user':forms.Select(attrs={'class': 'form-control'}), 

        }

class ReporteserviciosForm(forms.ModelForm):
    class Meta:
        model = ReporteServicios
        fields = [
            'eje_trabajo',
            'servicio',
            'fecha_inicio',
            'fecha_finalizacion',
            'presupuesto',
            'descripcion',
            'beneficiados', 
            'resultado',
            'user',
            ]

        labels = {
            'eje_trabajo':'Eje de trabajo',
            'servicio':'Servicio',
            'fecha_inicio':'Fecha de inicio',
            'fecha_finalizacion':'Fecha de finalizacion',
            'presupuesto':'Presupuesto',
            'descripcion':'Descripcion',
            'beneficiados':'Beneficiados', 
            'resultado':'Resultado',
            'user':'Usuario',
        }

        widgets = {

            'eje_trabajo':forms.Select(attrs={'class': 'form-control'}),
            'servicio':forms.TextInput(attrs={'class': 'form-control '}), 
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'fecha_finalizacion':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'presupuesto':forms.TextInput(attrs={'class': 'form-control '}), 
            'descripcion':forms.TextInput(attrs={'class': 'form-control '}), 
            'beneficiados':forms.TextInput(attrs={'class': 'form-control '}), 
            'resultado':forms.TextInput(attrs={'class': 'form-control '}), 
            'user':forms.Select(attrs={'class': 'form-control'}),

        }