from django.shortcuts import render
from .models import Product
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product

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
    product = Product.objects.all()
    return render(request, 'candlecare.html', {'product':product})

def shop_all(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 8)  # 8 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render(request, 'shopAll.html', {'products': products})

#comment