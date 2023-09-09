# from django.contrib.auth.models import User  # might change when we add our users
from django.conf import settings
from django.db import models
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


"""
Category - Model za Kategorije knjiga
@version 1.0
"""
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)  # might not be needed

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    # da ne bi nam sistem automatski napisao za Category, Categorys
    class Meta:
        verbose_name_plural = 'categories'


"""
Category - Model za produkte koji se prodaju, u nasem slucaju knjige. 
@version 1.0
"""


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # sortiranje podataka
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    # automatski generisemo url za knjigu, koriscenjem slug-a
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
