from venv import logger

from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  print('latest_question_list : ', latest_question_list)
  template = loader.get_template('polls/index.html') # polls/index.html 템플릿을 불러옴
  context = { # 위에서 불러온 index.html 템플릿에 context 전달.
    'latest_question_list': latest_question_list,
  }
  return HttpResponse(template.render(context, request))

def detail(request, question_id):
  return HttpResponse("Your're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id) 
