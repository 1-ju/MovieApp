from contextlib import redirect_stdout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse





# Create your views here.
def register(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
        
        login(request, user)
        
        return render(request, "home/index.html")
        
    else:
        return render(request, "authentication/register.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
        else:
            return HttpResponse("wrong username or password")
        
        return render(request, 'home/index.html')
    else:
        return render(request, "authentication/login.html")
    
def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')
