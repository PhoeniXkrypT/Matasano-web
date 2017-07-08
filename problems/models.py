# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SetOneQuestions(models.Model):
    qid = models.IntegerField()
    title = models.CharField(max_length=200)
    question = models.TextField(default='')
    answer = models.TextField(default='')

    def __str__(self):
        return self.title
