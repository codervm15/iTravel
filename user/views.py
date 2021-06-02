from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            if(not User.objects.filter(username=username).exists()):
                if(not User.objects.filter(email=email).exists()):
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)
                    user.save()
                    return redirect('/')
                else:
                    messages.info(request,'Email already exists')
                    return render(request,'register.html')
            else:
                messages.info(request,'Username already exists')
                return render(request,'register.html')
        else:
            messages.info(request,'Password mismatch')
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Inavlid Credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
