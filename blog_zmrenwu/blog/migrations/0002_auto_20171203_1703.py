# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='fen_lei',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]
