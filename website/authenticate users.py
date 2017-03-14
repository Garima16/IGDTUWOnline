from django.contrib.auth import authenticate
from django.contrib.auth.models import User

with open('credentials.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')
        username = data[0]
        password = data[1]
        user = User.objects.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        authenticate(username=username, password=password)





