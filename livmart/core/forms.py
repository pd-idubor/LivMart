from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


STYLES = 'w-full py-3 px-6 rounded-xl bg-white'

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'adam001',
        'class': STYLES
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'example@email.com',
        'class': STYLES
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': STYLES
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Repeat your password',
        'class': STYLES
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'adam001',
        'class': STYLES
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': STYLES
    }))
    class Meta:
        model = User
        fields = ['username', 'password']