from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_plural_name = "Categories"
        ordering = ['-created']

    def __str__(self):
        return self.category


class Product(models.Model):
    pass