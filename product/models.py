from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural  = "Categories"
        ordering = ['-created']

    def __str__(self):
        return self.category


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    availiability = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True) 

     # Generate random slugs
    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.product_name)

            has_slug = Product.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.slug) + '-' + str(count)
                has_slug = Product.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    # XXX For uploading more images for product model
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.URLField()

    def __str__(self):
        return f"New Image"

    