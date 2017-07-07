# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='tags',
        ),
        migrations.AddField(
            model_name='car',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]
