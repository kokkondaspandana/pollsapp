from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^student/', views.index),
    url(r'^addstudent/', views.addstudent),
    url(r'^newstudent/', views.newstudent),
]

