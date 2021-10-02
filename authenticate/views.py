from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render


def newuser(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('newuser')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist! Please try some other Email")
            return redirect('newuser')
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched")


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('signin')
    return render(request, "authenticate/newuser.html")

def welcome(request):
    return render(request, "authenticate/index.html")

def guest(request):
    return render(request, "authenticate/guest.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Succcessfully!")
    return redirect('welcome')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authenticate/index.html", {'fname': fname})
        else:
            messages.error(request, "Wrong credentials")
            return redirect('signin')
    return render(request, "authenticate/signin.html")



# Create your views here.
