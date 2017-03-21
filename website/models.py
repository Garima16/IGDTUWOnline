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


class Student(User):
    changed_password_atleast_once = models.BooleanField(default=False)

    def __str__(self):
        return self.username

