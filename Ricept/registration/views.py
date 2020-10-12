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
                messages.info(request, "Псевдоним занят")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email неверно указан или уже зарегистрирован")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password = password, email=email,first_name=username,last_name=username )
                user.save();
                return redirect("/")
        else:
            messages.info(request, "Пароли не совпадают")
            return redirect("register")
        print(username + " " + email)
    else:
        users = User.objects.all()
        for user in users:
            print(user.username)
        return render(request, "registration/register.html")


def login(request):
    return HttpResponse("success")
