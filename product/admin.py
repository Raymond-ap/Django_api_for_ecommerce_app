from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    models = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = (
        'product_name',
        'category',
        'price',
        'published',
        'created',
    )
    search_fields = (
        'product_name',
        'category',
        'price'
    )