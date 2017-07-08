
from django.shortcuts import render

def qa_view(request, question, qurl):
    html_template = 'problems/qa-template.html'
    if request.method == 'GET':
        context = {'question': question, 'qurl': qurl, 'status': ''}
        return render(request, html_template, context)
    elif request.method == 'POST':
        context = {'question': question, 'qurl': qurl, 'status': 'Wrong answer'}
        if request.POST.get('answer', '') == question.answer:
            context['status'] = 'Correct answer'
        return render(request, html_template, context)

