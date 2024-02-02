import random
from django.shortcuts import render,redirect
from django.http import HttpResponseNotAllowed
from django.contrib import auth

# Create your views here.
from accounts.models import User




def register(request):
    if request.method=='GET':
        return render(request,'register.html',{'title':'Chat Register'})
    elif request.method=='POST':
        username = request.POST.get('username', f'User{str(random.randint(0, 10000000000))}')
        email=request.POST.get('email', '')
        password = request.POST.get('password', '')
        User.objects.create_user(username=username, password=password,email=email)
        return redirect('login')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

            
    
    
def login(request):
    
    if request.method=='GET':
        return render(request,'login.html',{'title':'Chat Login'})
    elif request.method=='POST':
        email=request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    