# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]