from django.shortcuts import render
from .models import Product, Category, Brand
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'candlehome.html', {'featured_products': featured_products})

def shop_all(request):
    products = Product.objects.all()
    return render(request, 'shopAll.html', {'products':products})

def product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product.html', {'product':product})

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = 'New Contact Form Submission'
        message_content = f'Name: {full_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['naved.raveed@gmail.com']  #  admin's email

        send_mail(subject, message_content, from_email, recipient_list, fail_silently=False)

        return render(request, 'success.html')
    return render(request, 'contact.html')

def customcandles(request):
    return render(request, 'customcandles.html')

def candlecare(request):
    return render(request, 'candlecare.html')

def category(request, strtext):
    category = Category.objects.get(name=strtext)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products':products, 'category':category})

def brand(request, strtext):
    brand = Brand.objects.get(name=strtext)
    products = Product.objects.filter(brand=brand)
    return render(request, 'category.html', {'products':products, 'brand':brand})