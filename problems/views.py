# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SetOneQuestions

# Create your views here.

def index(request):
    problem_sets = {'Set1': 'Set 1: Basics', \
                    'Set2': 'Set 2: Block Crypto', \
                    'Set3': 'Set 3: Block and Stream Crypto', \
                    'Set4': 'Set 4: Stream Crypto and Randomness', \
                    'Set5': 'Set 5: Diffie-Hellman and friends', \
                    'Set6': 'Set 6: RSA and DSA', \
                    'Set7': 'Set 7: Hashes', \
                    'Set8': 'Set 8: Abstract Algebra'}
    context = {'problem_sets' : sorted(problem_sets.items())}
    return render(request, 'problems/index.html', context)

def set_one(request):
    questions = SetOneQuestions.objects.all()
    context = {'questions' : questions}
    return render(request, 'problems/set1.html', context)
