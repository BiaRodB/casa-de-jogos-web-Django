
from dataclasses import field
from django import forms
from jogos.models import Cliente, Bicho , Mega , Carteira
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
        email = forms.EmailField(required=True)

        class Meta:
                model = User
                fields = ['username']

class ClienteForm(forms.ModelForm):

        class Meta:
                model = Cliente
                fields = '__all__'

class MegaForm(forms.ModelForm):

        class Meta:
                model = Mega
                fields = '__all__'

class CarteiraForm(forms.ModelForm):
    
    class Meta:
        model = Carteira
        fields = '__all__'


class BichoForm(forms.ModelForm):
        class Meta:
                model = Bicho
                fields ='__all__'
