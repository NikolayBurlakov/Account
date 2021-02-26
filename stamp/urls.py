from django.contrib import admin
from django.urls import path, include
from stamp.views import *

app_name = 'stamp'
urlpatterns = [
    path('plotter/create/', PlotterCreateView.as_view()),
    path('plotter/list/', PlotterListView.as_view()),
    path('plotter/detail/<int:pk>/', PlotterListView.as_view()),

    path('mold/create/', MoldCreateView.as_view()),
    path('mold/list/', MoldListView.as_view()),
    path('mold/detail/<int:pk>/', MoldListView.as_view()),

    path('user/create/', UserCreateView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserListView.as_view()),

    path('diller/create/', DillerCreateView.as_view()),
    path('diller/list/', DillerListView.as_view()),
    path('diller/detail/<int:pk>/', DillerDeteilView.as_view()),
]
