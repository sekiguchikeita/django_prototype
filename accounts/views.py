from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.htm', {'error':'このアドレスは既に使われています'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.htm', {'error':'パスワードが間違っています'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.htm')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.htm', {'error':'メールアドレスもしくはパスワードが間違っています'})
    else:
        return render(request, 'accounts/login.htm')



def logout(request):
    #to do need to route to homepage
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


