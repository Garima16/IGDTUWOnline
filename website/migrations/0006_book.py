# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0005_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('writer', models.CharField(max_length=20)),
            ],
            options={
                'managed': True,
                'db_table': 'Books',
            },
        ),
    ]
