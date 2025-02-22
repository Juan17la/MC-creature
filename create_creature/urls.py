from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collection/', views.collections, name = 'collection'),
    path('generate/', views.generate, name='generate'),
    path('singout/', views.singout, name = 'singout'),
    path('singin/', views.singin, name = 'singin'),
    path('singup/', views.singUp, name = 'singup'),
]
