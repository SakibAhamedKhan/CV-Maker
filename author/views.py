from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from .models import UserInfo
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
            user=form.save()
            username =  form.cleaned_data.get('username')
            ui = UserInfo(user=user, location="Not set yate")
            ui.save()
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'author/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request, 'author/profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'core/home.html')