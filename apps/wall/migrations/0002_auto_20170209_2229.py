# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pw_hash',
            new_name='password',
        ),
    ]