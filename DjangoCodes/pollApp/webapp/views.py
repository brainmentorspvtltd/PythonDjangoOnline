from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
def index(req):
    ques = Question.objects.all()
    # print(ques)
    return render(req, 'index.html', {'questions':ques})

def details(req, question_id):
    ques = Question.objects.get(pk=question_id)
    return render(req, 'details.html', {'question':ques})