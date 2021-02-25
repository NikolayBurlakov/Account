from django.contrib import admin
from django.urls import path, include
from stamp.views import *

app_name = 'stamp'
urlpatterns = [
    path('plotter/create/', PlotterCreateView.as_view()),
    path('mold/create/', MoldCreateView.as_view()),

    path('user/create/', UserCreateView.as_view()),
    path('user/list_all/', UserListView.as_view()),

    path('diller/create/', DillerCreateView.as_view()),
    path('diller/list_all/', DillerListView.as_view()),
    path('diller/detail/', DillerDeteilView.as_view()),
]