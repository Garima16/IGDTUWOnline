# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-21 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_student_has_logged_in_first_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
