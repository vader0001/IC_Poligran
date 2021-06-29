from django import forms
from .models import Customer
from django.forms.widgets import PasswordInput

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')
    email = forms.CharField(max_length=100, label='E-Mail')
    address = forms.CharField(max_length=100, label='Dirección')
    city = forms.CharField(max_length=50, label='Ciudad')
    department = forms.CharField(max_length=50, label='Departamento')
    password = forms.CharField(widget=PasswordInput, label='Clave secreta')

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "address", "email", "city", "department", "password"]