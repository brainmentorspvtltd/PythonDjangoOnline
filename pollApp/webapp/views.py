from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def index(req):
    ques = Question.objects.all()
    # print(ques)
    return render(req, 'index.html', {'questions':ques})

def details(req, question_id):
    ques = Question.objects.get(pk=question_id)
    return render(req, 'details.html', {'question':ques})

def result(req, question_id):
    ques = Question.objects.get(pk=question_id)
    return render(req, 'result.html', {'question':ques})

def vote(req, question_id):
    ques = Question.objects.get(pk=question_id)
    errorMessage = 'Please Select one choice'
    try:
        selected_choice = ques.choice_set.get(pk = req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print("Exception Occurred...")
        # return render(req, 'details.html', {
        #     'ques' : ques,
        #     'errorMessage' : 'Please Select one choice'
        # })
        return HttpResponseRedirect(reverse('pollApp:detail', args=(question_id,)))
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # return render(req, 'result.html', {'question': ques})
        return HttpResponseRedirect(reverse('pollApp:result', args=(question_id,)))