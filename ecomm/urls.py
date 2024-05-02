from django.urls import path
from .views import *

urlpatterns = [
    # category urls
    path('category/', CategoryList.as_view(), name = 'category list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name = 'category detail'),

    # products urls
    path('products/', ProductList.as_view(), name = 'product list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name = 'product detail'),

    # orders urls
    path('order/', OrderPlaced.as_view(), name = 'order list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name = 'order detail'),
] 