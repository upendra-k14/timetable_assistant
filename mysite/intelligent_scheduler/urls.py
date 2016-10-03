from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index1$', views.index1, name='index1'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^index3$', views.index3, name='index3'),
    url(r'^index4$', views.index4, name='index4'),
    url(r'^index5$', views.index5, name='index5'),
    url(r'^index6$', views.index6, name='index6'),
    url(r'^index7$', views.index7, name='index7'),
    url(r'^fullcalendar$', views.fullcalendar, name='fullweekcalendar'),
]
