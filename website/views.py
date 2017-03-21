from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Book, Student
from .forms import UserLoginForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import password_strength_ok


def home(request):
    books = Book.objects.all()
    for book in books:
        print(book)
    return render(request, 'website/books.html', {'books': books})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
<<<<<<< HEAD
        user = Student.objects.get(username=username)
        if not user.changed_password_atleast_once:
            return redirect('website.views.change_password')
=======
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
        user = Student.objects.get(username=username)
        if not user.changed_password_atleast_once:
            if not user.has_logged_in_first_time:
                user.has_logged_in_first_time = True
                user.save()
                return redirect('website.views.set_password_unusable')
>>>>>>> 1eaa382a8e7d781a678bd7fe33db1d2d3a11e81f
        return redirect('website.views.home')
    return render(request, 'website/login.html', {"form": form})


def change_password(request):
    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
<<<<<<< HEAD
        user = request.user
        username = user.username
=======
        #user = request.user
        username = form.cleaned_data.get("username")
        user = Student.objects.get(username=username)
>>>>>>> 1eaa382a8e7d781a678bd7fe33db1d2d3a11e81f
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
        user.changed_password_atleast_once = True
        user.save()
<<<<<<< HEAD
        return redirect('website.views.home')
    return render(request, "website/change_password.html", {"form": form})

=======
        print(user.changed_password_atleast_once)
        return redirect('website.views.home')
    return render(request, "website/change_password.html", {"form": form})


def set_password_unusable(request):
    user = request.user
    user.set_unusable_password()
    user.save()
    return redirect('website.views.change_password')

>>>>>>> 1eaa382a8e7d781a678bd7fe33db1d2d3a11e81f
