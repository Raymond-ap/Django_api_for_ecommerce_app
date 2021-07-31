from django.http import JsonResponse, request
from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product, Category
from product.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def APIOVERVIEW(request):
    api_urls = {
        "Products": "/products_all",
        "Single Product Detail": "/product_detail/id/"
    }
    return JsonResponse(api_urls)


@api_view(["GET", "POST"])
def PRODUCTSVIEW(request):
    products = Product.objects.filter(published=True);
    serializers = ProductSerializer(products, many=True);
    return Response(serializers.data)


@api_view(["GET", "POST"])
def PRODUCTDETAIL(request, id):
    product = Product.objects.get(id=id, published=True)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)