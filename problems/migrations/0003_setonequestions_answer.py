# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20170708_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='setonequestions',
            name='answer',
            field=models.TextField(default=''),
        ),
    ]