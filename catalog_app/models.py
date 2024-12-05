from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog_app:category_items", kwargs={
            'slug': self.slug
        })

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=16)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog_app:item", kwargs={
            'sku': self.sku
        })

class ItemImage(models.Model):
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.item.name