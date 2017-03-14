from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from website.models import Student

#with open('credentials.txt', 'r') as file:
#file=[]
file = [['aalo', 'aalo'], ['gjain', 'gjain'], ['shreya', 'shreya'], ['goma', 'goma'], ['me', 'me']]
#file=[['goma', 'goma'], ['sheldon', 'sheldon']]
for line in file:
        #data = line.strip().split(',')
    username = line[0]
    password = line[1]
    user = Student.objects.create_user(username=username, password=password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
        #authenticate(username=username, password=password)

