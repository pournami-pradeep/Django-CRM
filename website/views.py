from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully.")
            return redirect('home')
        messages.success(request,"Error logging in.")
        return redirect('home')
    return render(request, 'home.html',{})
