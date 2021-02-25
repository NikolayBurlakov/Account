from django.shortcuts import render
from rest_framework import generics
from stamp.serializers import *


class DillerCreateView(generics.CreateAPIView):
    serializer_class = DillerDetailSerializer


# class DillerListView(generics.ListAPIView):
#     serializer_class =

class PlotterCreateView(generics.CreateAPIView):
    serializer_class = PlotterDetailSerializer


class MoldCreateView(generics.CreateAPIView):
    serializer_class = MoldDetailSerializer
