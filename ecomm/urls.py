from django.urls import path
from .views import *

urlpatterns = [
    path('category/', ListCategory.as_view(), name = 'category list'),
    path('category/<slug:val>/', DetailCategory.as_view(), name = 'category detail'),
] 