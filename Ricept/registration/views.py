from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.contrib.auth.models import  User, auth


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password == password_confirmation and password != "":
            if User.objects.filter(username=username).exists() or username == "":
                messages.info(request, "Ім'я користувача зайняте")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email вказано невірно, або вже зареєстровано")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password = password, email=email,first_name=username,last_name=username )
                user.save();
                return redirect("login")
        else:
            messages.info(request, "Паролі не збігаються")
            return redirect("register")
    else:
        return render(request, "registration/register.html")


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Введено невірний email або пароль")
            return redirect("login")
    else:
        return render(request,"registration/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')