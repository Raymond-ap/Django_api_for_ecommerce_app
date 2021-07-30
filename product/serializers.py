from django.db import models
from django.db.models import fields
from .models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
