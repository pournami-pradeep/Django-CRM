from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from website.models import Record

from .forms import RecordForm, UserSignUpForm

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
    return render(request, 'home.html',{"records":records})

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
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registered successfully.")
            return redirect('home')
        
        return render(request,'register.html',{'form':form})
    
    form = UserSignUpForm()
    return render(request,'register.html',{'form':form})

def add_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Created successfully.")
            return redirect('home')
        return render(request,'add_record.html',{'form':form})
    form = RecordForm()
    return render(request,'add_record.html',{'form':form})
        

def customer_record(request,pk):
    if request.user.is_authenticated:
        try:
            record = Record.objects.get(id=pk)
        except:
            return render(request,'page_not_found.html',{})
        
        return render(request,'record.html',{'record':record})
    messages.success(request,"Please Log in")
    return render(request, 'home.html',{})

def delete_record(request,pk):
    if request.user.is_authenticated:
        try:
            record = Record.objects.get(id=pk)
        except:
            return render(request,'page_not_found.html',{})
        record.delete()
        messages.success(request,"Record deleted successfully.")
        return redirect('home')
    messages.success(request,"Please Log in")
    return render(request, 'home.html',{})
        




