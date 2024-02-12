from django.db import models
# from django.utils.text import slugify
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# import datetime


class Brand(models.Model):
  name = models.CharField(max_length=50, default='', blank='True')
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50, default='', blank='True')
  def __str__(self):
    return self.name

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

# date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    username = models.CharField(max_length=100)
    rating = models.IntegerField(default=5, blank=True, null=True)
    userreview = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.username} - {self.userreview}'