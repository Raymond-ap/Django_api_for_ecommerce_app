from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('', APIOVERVIEW, name="Overview"),
    path('products_all', PRODUCTSVIEW, name="products_all"),
    path('product_detail/<str:id>/', PRODUCTDETAIL, name="product_detail"),
]
