# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class publisherInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, unique=True )

class bookInfo(models.Model):
    id=models.AutoField(primary_key=True)
    bookName=models.CharField(max_length=64)
    publisher=models.ForeignKey(to='publisherInfo')

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=48)
    book = models.ManyToManyField(to='bookInfo')

    def __str__(self):
        return 'Author Object:{}'.format(self.aname)