# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SetOneQuestions

# Create your views here.

def index(request):
    problem_sets = ['Set 1', 'Set 2', 'Set 3', 'Set 4']
    context = {'problem_sets' : problem_sets}
    return render(request, 'problems/index.html', context)

def set_one(request):
    questions = SetOneQuestions.objects.all()
    context = {'questions' : questions}
    return render(request, 'problems/set1.html', context)
