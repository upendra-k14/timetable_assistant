from django.shortcuts import render
from django.http import HttpResponse

def fullcalendar(request):
    return render(request,'intelligent_scheduler/fullweekcalendar.html')

def index (request):
    return render(request,'intelligent_scheduler/index.html')
