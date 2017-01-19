from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Book
from .forms import UserLoginForm

# Create your views here.


def home(request):
    books = Book.objects.all()
    return render(request, 'website/home.html', {'books': books})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, 'website/login.html', {"form": form})
