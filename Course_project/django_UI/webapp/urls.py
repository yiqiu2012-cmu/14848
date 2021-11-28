from django.contrib import admin
from django.urls import path
from toolbox import views

urlpatterns = [
    path('open_hadoop', views.open_hadoop, name='open_hadoop'),
    path('open_spark', views.open_spark, name='open_spark'),
    path('open_jupyter', views.open_jupyter, name='open_jupyter'),
    path('open_sonarqube', views.open_sonarqube, name='open_sonarqube'),
    path('', views.home),
]
