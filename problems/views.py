# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    problem_sets = ['Set 1', 'Set 2', 'Set 3', 'Set 4']
    context = {'problem_sets' : problem_sets}
    return render(request, 'problems/index.html', context)


