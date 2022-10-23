from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
  last_question_list = Question.objects.all()
  return render(request,"polls/index.html", {
    "last_question_list": last_question_list
  })

def detail(request, question_id):
  return HttpResponse(f"Estas viendo las opciones de la pregunta numero{question_id}")


def results(request, question_id):
  return HttpResponse(f"Estas viendo las opciones de la pregunta numero{question_id}")