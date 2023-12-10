from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import CostsModel
from .serializers import CostsModelSerializer


class InfoAboutСosts(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostsModel.objects.all()
    serializer_class = CostsModelSerializer


class CreateAboutCosts(generics.CreateAPIView):
    queryset = CostsModel.objects.all()
    serializer_class = CostsModelSerializer


