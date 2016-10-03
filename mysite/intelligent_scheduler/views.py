from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return render(request,'intelligent_scheduler/weekcalendar.html')

def index2(request):
    return render(request,'intelligent_scheduler/weekcalendar_json.html')

def index3(request):
    return render(request,'intelligent_scheduler/weekcalendar_dst.html')

def index4(request):
    return render(request,'intelligent_scheduler/weekcalendar_demo_4.html')

def index5(request):
    return render(request,'intelligent_scheduler/weekcalendar_demo_3.html')

def index6(request):
    return render(request,'intelligent_scheduler/weekcalendar_demo_2.html')

def index7(request):
    return render(request,'intelligent_scheduler/index7.html')

def fullcalendar(request):
    return render(request,'intelligent_scheduler/fullweekcalendar.html')
