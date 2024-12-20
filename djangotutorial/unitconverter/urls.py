from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("temp/", views.temp, name='temp'),
    path("length/", views.length, name='length'),
    path("weight/", views.weight, name='weight'),
    path("answer/", views.answer, name='answer')

]
