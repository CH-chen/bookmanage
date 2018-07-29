# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-11 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='bookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=64)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book01.publisherInfo')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='book01.bookInfo'),
        ),
    ]