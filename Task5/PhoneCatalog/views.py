from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import table
from django.template import loader


# def index(request):
#      return HttpResponse("Hello World")

# def index(request):
#     latest_question_list = table.objects.order_by('-pub_date')[:1]
#     # output = ', '.join([q.Name for q in latest_question_list])
#     return HttpResponse(latest_question_list)

def index(request):
    peopless = table.objects.all()
    return render(request, 'C:/ycheba/python/python/Task5/PhoneCatalog/templates/table.html', locals())



