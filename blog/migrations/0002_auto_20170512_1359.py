# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='port',
            new_name='Post',
        ),
    ]
