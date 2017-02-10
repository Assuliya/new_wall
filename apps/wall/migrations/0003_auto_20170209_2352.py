# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 23:52
from __future__ import unicode_literals

import apps.wall.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20170209_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, validators=[apps.wall.models.uniqueEmail]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, validators=[apps.wall.models.moreThanTwo]),
        ),
    ]