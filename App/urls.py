from django.urls import path
from . import views

urlpatterns = [
    path('', views.App, name='App'),
    path('BienvenidaApp/', views.BienvenidaApp, name='BienvenidaApp'),
]

