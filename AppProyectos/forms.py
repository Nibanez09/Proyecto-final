from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
# Create your forms here.

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    empresa = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    email = forms.EmailField()

class ProyectoForm(forms.Form):
    codigo = forms.CharField(max_length=40)
    fecha_recibido = forms.DateField()
    plazo = forms.IntegerField()
    categoria = forms.CharField(max_length=40)

class ResponsableForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)

class RegistroFormulario(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingresar contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class FormularioEditar(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingresar contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
