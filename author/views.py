from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout, authenticate, login
from .models import UserInfo, CustomUser, ContactUs
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(request):
    if request.method=='POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
            user=form.save()
            username =  form.cleaned_data.get('username')
            ui = UserInfo(user=user)
            ui.save()
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'author/register.html', {'form':form})

@login_required
def profilepage(request):
    userInfo = UserInfo.objects.get(user=request.user)
    if request.method=='POST':
        img = request.FILES.get('image', None)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        age = request.POST.get('age')
        birth_date = request.POST.get('birth_date')
        education = request.POST.get('education')
        country = request.POST.get('country')
        state = request.POST.get('state')
        userInfo = UserInfo.objects.get(user=request.user)
        
        if img!=None:
            userInfo.image=img
        userInfo.education=education
        userInfo.country=country
        userInfo.state=state
        userInfo.save()

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.address = address
        user.zip_code = zip_code
        user.age = age
        user.birth_date = birth_date
        user.save()


        messages.success(request, f'Successfully updated your profile!')
        return redirect('profile')
    
    return render(request, 'author/profile.html', {'userInfo':userInfo})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                messages.success(request, f'Success fully logged {name}!')
                return redirect('home')
        else:
            messages.warning(request, 'Login informtion incorrect') 
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'author/login.html', {'form': form})

            
def logout_view(request):
    logout(request)
    return render(request, 'core/home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message)
        ContactUs.objects.create(name = name, email= email, phone = phone, message = message)
        messages.success(request, f'Successfully submited {name}!')


    return render(request, 'author/contact.html')

def about(request):
    return render(request, 'author/about.html')