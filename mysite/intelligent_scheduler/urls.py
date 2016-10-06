from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fullcalendar$', views.fullcalendar, name='fullweekcalendar'),
    url(r'^index$', views.index, name='index'),
]
