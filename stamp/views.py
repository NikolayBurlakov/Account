from django.shortcuts import render
from rest_framework import generics
from stamp.serializers import DillerDetailSerializer, UserDetailSerializer
# Create your views here.


class StampCreateView(generics.CreateAPIView):
    serializer_class = DillerDetailSerializer


