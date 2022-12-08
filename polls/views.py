from venv import logger

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  print('latest_question_list : ', latest_question_list)
  # template = loader.get_template('polls/index.html') # polls/index.html 템플릿을 불러옴
  context = { # 위에서 불러온 index.html 템플릿에 context 전달.
    'latest_question_list': latest_question_list,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'polls/index.html', context)
  

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id) #객체가 없을경우 Http404 예외 발생
  # return HttpResponse("Your're looking at question %s." % question_id)
  return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
  # response = "You're looking at the results of question %s."
  question = Question.objects.get(pk=question_id)
  # return HttpResponse(response % question_id)
  return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
  question = Question.objects.get(pk=question_id)
  # return HttpResponse("You're voting on question %s." % question_id) 
  return render(request, 'polls/vote.html', {'question':question}) 
