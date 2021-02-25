from django.shortcuts import render
from rest_framework import generics
from stamp.serializers import *


# Diller
class DillerCreateView(generics.CreateAPIView):
    serializer_class = DillerDetailSerializer
    queryset = Diller.objects.all()


class DillerListView(generics.ListAPIView):
    serializer_class = DillerListSerializer
    queryset = Diller.objects.all()


class DillerDeteilView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DillerDetailSerializer
    queryset = Diller.objects.all()


# Plotter
class PlotterCreateView(generics.CreateAPIView):
    serializer_class = PlotterDetailSerializer
    queryset = Plotter.objects.all()


# User
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Users.objects.all()


# Mold
class MoldCreateView(generics.CreateAPIView):
    serializer_class = MoldDetailSerializer
