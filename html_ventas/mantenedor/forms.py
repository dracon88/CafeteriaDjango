from django import forms
from django.core import validators
from .models import Registrado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email", "clave"]


	


class RegisterForm(UserCreationForm):

	class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
