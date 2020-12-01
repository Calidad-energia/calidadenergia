from django import forms
from django.contrib.auth.models import User
from .models import *
from firebase import firebase

class login_form(forms.Form):
    user        = forms.CharField(widget = forms.TextInput())
    password    = forms.CharField(label='Contraseña',widget = forms.PasswordInput(render_value=False))

class registro_form(forms.Form):
    name        = forms.CharField(widget= forms.TextInput())
    email       = forms.EmailField(widget= forms.TextInput())
    password_1  = forms.CharField(label='Password',widget= forms.PasswordInput(render_value=False))
    password_2  = forms.CharField(label='Confirmar Password',widget= forms.PasswordInput(render_value=False))

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            u = User.objects.get(username=name)
        except User.DoesNotExist:
            return name
        raise forms.ValidationError('Nombre ya registrado')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Ya existe correo')

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 == password_2 :
            pass
        else:
            raise forms.ValidationError('No coinciden las contraseñas')

# class Perfil_Form(forms.ModelForm):
#     class Meta:
#         model= Perfil
#         fields = '__all__'
#         exclude = ['user']