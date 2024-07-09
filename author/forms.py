from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control bg-transparent', 
        'placeholder': 'Email'
    }))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent', 
        'placeholder': 'Address'
    }))
    zip_code = forms.CharField(max_length=5, widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent', 
        'placeholder': 'Zip Code'
    }))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control bg-transparent',
        'placeholder': 'Birth Date'
    }))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control bg-transparent',
        'placeholder': 'Age'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-transparent',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-transparent',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control bg-transparent',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'address', 'zip_code', 'birth_date', 'age']

    