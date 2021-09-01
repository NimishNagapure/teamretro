from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RetroUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text='Required')

    class Meta:
        model = RetroUser  
        fields = ('email','username','password1','password2')
