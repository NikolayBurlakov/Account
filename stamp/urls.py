from django.contrib import admin
from django.urls import path, include
from stamp.views import *

app_name = 'stamp'
urlpatterns = [
    path('stamp/create/', StampCreateView.as_view())
]