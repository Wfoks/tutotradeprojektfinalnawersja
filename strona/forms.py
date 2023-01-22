from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class OglosznieForm(ModelForm):
    class Meta:
        model = Ogloszenie
        fields = ['przedmiot','zakres_materialu','zagadnienie']

class NauczajOglosznieForm(ModelForm):
    class Meta:
        model = NauczajOgloszenie
        fields = ['przedmiot','zakres_od','zakres_do']

class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  


class ThreadForm(forms.Form):
    username = forms.CharField(label='',max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)
    

