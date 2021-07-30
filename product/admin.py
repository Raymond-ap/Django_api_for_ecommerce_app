from django.contrib import admin
from .models import Product, ProductImage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created', 'modified')
    search_fields = ('category',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
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


admin.site.register(Product, ProductAdmin)