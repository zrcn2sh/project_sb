# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
