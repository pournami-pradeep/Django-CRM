from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from website.models import Record

from .forms import UserSignUpForm

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully.")
            return render(request, 'home.html',{"records":records})
        messages.success(request,"Error logging in.")
        return redirect('home')
    return render(request, 'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"Loged out successfully.")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            print(form.cleaned_data)
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registered successfully.")
            return redirect('home')
        
        return render(request,'register.html',{'form':form})
    
    form = UserSignUpForm()
    return render(request,'register.html',{'form':form})


