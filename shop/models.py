from django.db import models
import datetime


class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(max_length=10)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=12)

  def __str__(self):
    return f'{self.firstname} + {self.lastname}'

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
  ingredients = models.CharField(max_length=100, default='Vanilla')
  description = models.CharField(max_length=250, default='', blank='True')
  image1 = models.ImageField(upload_to='uploads/products')
  image2 = models.ImageField(upload_to='uploads/products', blank='True', null='True')
  image3 = models.ImageField(upload_to='uploads/products', blank='True', null='True')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
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