from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


class Brand(models.Model):
  name = models.CharField(max_length=50, default='', blank='True')
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50, default='', blank='True')
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50, default='', blank='True')
  def __str__(self):
    return f'{self.firstname} + {self.lastname}'

class Product(models.Model):
  slug = models.SlugField(max_length=255, blank=True)
  name = models.CharField(max_length=255, unique=True)
  price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
  ingredients = models.CharField(max_length=100, default='Vanilla')
  description = models.CharField(max_length=250, default='', blank='True')
  image1 = models.ImageField(upload_to='uploads/products')
  image2 = models.ImageField(upload_to='uploads/products', blank='True', null='True')
  image3 = models.ImageField(upload_to='uploads/products', blank='True', null='True')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None)
  is_featured = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class OrderDetails(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  address = models.CharField(max_length=100, default='', blank=False)
  phone = models.CharField(max_length=20, default='', blank='True')
  date = datetime.datetime.today
  status = models.BooleanField(default=False)

  def __str__(self):
    return self.product

class Review(models.Model):
    user_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user_name} - {self.content}'