# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE,)
    publication_date = models.DateField()

    def __unicode__(self): # __str__ on Python 3
        return self.title

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __unicode__(self): # __str__ on Python 3
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __unicode__(self): # __str__ on Python 3
        return self.name





