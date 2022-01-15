from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profiles (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return self.user

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)



class Category(models.Model):
    name = models.CharField(max_length=700, db_index=True, null=True)
    slug = models.SlugField(max_length=700, unique=True)

    class meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('market:category_list', args=[self.slug])

    def __str__(self):
        return self.name




class Product (models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator', null=True)
    title = models.CharField(max_length=700)
    author = models.CharField(max_length=700, default='admin')
    description = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=700)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('market:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
