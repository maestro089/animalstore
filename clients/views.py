from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from store.models import Product


def log_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        check = User.objects.filter(email=email)
        if check:
            context = {"message": "Пользователь с такой почтой уже существует!"}
            return render(request, "logup.html", context)

        user = User.objects.create_user(username, email, password)

        if user is not None and user.is_active:
            user.save()
            return render(request, "store/index.html")
        return render(request, "logup.html")
    return render(request, "logup.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            products = Product.objects.all()
            context = {"products": products}
            return render(request, "store/index.html", context)
        return render(request, "login.html")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/index.html", context)
