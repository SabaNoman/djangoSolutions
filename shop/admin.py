from django.contrib import admin
from shop.models import Category, Product, Customer, OrderDetails, Brand ,Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderDetails)
admin.site.register(Brand)
admin.site.register(Review)