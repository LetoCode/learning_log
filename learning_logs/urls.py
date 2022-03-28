"""Определяет схемы URL для приложения learnin_log"""

from django.urls import path

from . import views

app_name = 'learing_logs'
urlpatterns = [
    path('', views.index, name='index')
    #Страница со списком всех тем
    path('topics/', views.topics, name='topics')
]
