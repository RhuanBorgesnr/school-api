from django.urls import path 
from .views import *

from . import views


urlpatterns = [
    path('', views.aulas, name='aulas'),
    path('alunos/', views.alunos, name='alunos'),


]