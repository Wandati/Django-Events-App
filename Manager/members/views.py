from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def register_user(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(request,username=username,password=password)
            # login(request,user)
            # messages.success(request,"Registration Successful! ")
            # return redirect("home")
            messages.success(request,"Registration Successful! Login to Continue.")
            return redirect("login_user")
    else:
        # form=UserCreationForm()
        form=RegisterUserForm()
    return render(request,"authenticate/register.html",{"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,"Login successful!")
            login(request,user)
            print(messages.get_messages(request))
            return redirect('home')
        else:
            messages.error(request,"login failed.invalid username or password!")
            return redirect("login_user")
        
    else:
        return render(request,"authenticate/login.html")
    
    
def logout_user(request):
    logout(request)
    messages.success(request,"logout successful.See you next time!")
    return redirect("home")