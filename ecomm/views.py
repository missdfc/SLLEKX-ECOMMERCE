from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import *

# category list views
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# category detail views
class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


# product list views
class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

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
class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

# product detail views
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

# ordes detail views
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderPlaced.objects.all()
    serializer_class = OrderPlacedSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        item = self.kwargs.get('item_pk')
        order = OrderPlaced.objects.get(pk=pk, user=self.request.user)
        if item == order.items.get(pk=item):
            return OrderPlaced.objects.filter(user=self.request.user)
        else:
            print('order item not found')
    
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        if not request.user.is_staff:
            return Response({'detail': 'You are not authorized to perform this action.'},) #status=status.HTTP_401_UNAUTHORIZED)
        else:
            return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status.lower() == 'pending':
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({'detail': 'Cannot delete order with status other than "pending".'},) #status=status.HTTP_400_BAD_REQUEST)