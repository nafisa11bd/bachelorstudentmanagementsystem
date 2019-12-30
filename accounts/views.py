from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect.'})

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def student(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/student.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:

              user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'],is_staff=False)

              auth.login(request,user)
              return redirect('home')
        else:
            return render(request,'accounts/student.html',{'error':'Passwords Must Match'})
    else:
        return render(request, 'accounts/student.html')

def teacher(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/teacher.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
              user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'],is_staff=True)
              auth.login(request,user)
              return redirect('home')
        else:
            return render(request,'accounts/teacher.html',{'error':'Passwords Must Match'})
    else:
        return render(request, 'accounts/teacher.html')

def courseadvisor(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/courseadvisor.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
              user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
              auth.login(request,user)
              return redirect('home')
        else:
            return render(request,'accounts/courseadvisor.html',{'error':'Passwords Must Match'})
    else:
        return render(request, 'accounts/courseadvisor.html')


