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

# cproduct list views
class ListProduct(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        search_term = self.request.query_params.get('search')

        # print('Search term:', search_term)
        if search_term:
            queryset = Product.objects.filter(name__icontains=search_term)
            print('filtered queryset:', queryset)
            return queryset
        else:
            return Product.objects.all()

# product list by category views
class ListProduct(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']

# product detail views
class DetailCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 