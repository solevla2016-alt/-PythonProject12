from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

            # EMAIL после регистрации
            send_mail(
                subject="Регистрация успешна",
                message="Добро пожаловать на сайт!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )

            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})



def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Неверный email или пароль")

    return render(request, "users/login.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def profile_view(request):
    return render(request, "users/profile.html")

