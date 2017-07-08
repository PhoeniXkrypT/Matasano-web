
from django.shortcuts import render
from django.views import View

from .forms import AnswerForm

def qa_view(request, question, qurl):
    html_template = 'problems/qa-template.html'
    answer_form = AnswerForm()
    if request.method == 'GET':
        context = {'question': question, 'qurl': qurl, 'status': '', 'answer_form': answer_form}
        return render(request, html_template, context)
    elif request.method == 'POST':
        context = {'question': question, 'qurl': qurl, 'status': 'Wrong answer', 'answer_form': answer_form}
        if request.POST.get('answer', '') == question.answer:
            context['status'] = 'Correct answer'
        return render(request, html_template, context)

