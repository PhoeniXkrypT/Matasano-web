# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setonequestions',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='setonequestions',
            name='question',
            field=models.TextField(default=''),
        ),
    ]