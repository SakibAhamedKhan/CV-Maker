from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    zip_code = forms.CharField(max_length=5)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    age = forms.IntegerField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'address', 'zip_code', 'birth_date', 'age']