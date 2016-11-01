from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Correo Electronico',
            'domicilio': 'Domicilio',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascota',
            'razones',
        ]

        labels = {
            'numero_mascota': 'Numero de Mascotas',
            'razones': 'Razones para Adoptar',
        }

        widgets = {
            'numero_mascota': forms.TextInput(attrs={'class': 'form-control'}),
            'razones': forms.Textarea(attrs={'class': 'form-control'}),
        }