from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Books'
        app_label = 'website'


"""
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        managed = True
        db_table = 'Persons'
        app_label = 'website'

"""


class Student(User):
    has_logged_in_first_time = models.BooleanField(default=False)
    changed_password_atleast_once = models.BooleanField(default=False)

    def __str__(self):
        return self.username

