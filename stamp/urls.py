from django.contrib import admin
from django.urls import path, include
from stamp.views import *

app_name = 'stamp'
urlpatterns = [
    path('diller/create/', DillerCreateView.as_view()),
    path('plotter/create/', PlotterCreateView.as_view()),
    path('mold/create/', MoldCreateView.as_view()),
]