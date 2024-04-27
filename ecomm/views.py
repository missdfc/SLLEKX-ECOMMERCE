from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# category list views
class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# category detail views
class DetailCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
