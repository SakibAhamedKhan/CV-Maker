from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from .models import UserInfo, CustomUser
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

def logout_view(request):
    logout(request)
    return render(request, 'core/home.html')