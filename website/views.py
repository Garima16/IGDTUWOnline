from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Book, Student
from .forms import UserLoginForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import password_strength_ok
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    books = Book.objects.all()
    for book in books:
        print(book)
    return render(request, 'website/books.html', {'books': books})


"""
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = verify(username, password) # function in utils.py
        if user is False:
            messages.error(request, 'Invalid username or password.Try again!')
            return render(request, 'website/login.html', {"form": form})
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("website.views.home")
    return render(request, 'website/login.html', {"form": form})
"""


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print("user:", user)
        user = Student.objects.get(username=username)
        print("before condition", user.has_logged_in_first_time, user.changed_password_atleast_once)
        if not user.changed_password_atleast_once:
            if not user.has_logged_in_first_time:
                user.has_logged_in_first_time = True
                user.save()
                return redirect('website.views.set_password_unusable')
        print('going there')
        # user.is_logging_in_first_time = False
        return redirect('website.views.home')
    return render(request, 'website/login.html', {"form": form})


def change_password(request):
    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
        #user = request.user
        username = form.cleaned_data.get("username")
        user = Student.objects.get(username=username)
        print(user)
        print("username:", username)
        password = form.cleaned_data.get("new_password")
        if not password_strength_ok(password):
            messages.error(request, 'Choose a strong password')
            return render(request, "website/change_password.html", {"form": form})
        confirm_password = form.cleaned_data.get("confirm_password")
        if confirm_password != password:
            messages.error(request, 'Passwords didn\'t match' )
            return render(request, "website/change_password.html", {"form": form})
        user.set_password(password)
        user.save()
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        messages.success(request, 'Password was successfully changed!')
        user = Student.objects.get(username=username)
        print("from change_password_view", user)
        user.changed_password_atleast_once = True
        user.save()
        print(user.changed_password_atleast_once)
        # user.is_logging_in_first_time = True
        return redirect('website.views.home')
    return render(request, "website/change_password.html", {"form": form})


"""
def if_logging_for_first_time(request):
    user = request.user
    user = Student.objects.get(username=user.username)
    if user.is_logging_in_first_time:
        return redirect('website.views.change_password')
"""


def set_password_unusable(request):
    user = request.user
    user.set_unusable_password()
    user.save()
    print("password set unusable")
    return redirect('website.views.change_password')

