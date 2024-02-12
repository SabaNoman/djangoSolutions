from django.shortcuts import render
from .models import Product, Category, Brand, Review
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product, Review
from .form import ReviewForm

def homepage(request):
    featured_products = Product.objects.filter(is_featured=True)
    reviews = Review.objects.all()[:5]  # Fetch the first five reviews
    return render(request, 'candlehome.html', {'featured_products': featured_products, 'reviews': reviews})

def shop_all(request):
    all_products = Product.objects.all().order_by('id')
    paginator = Paginator(all_products, 8)  # Eight products per page
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


def shop_category(request, strtext):
    strtext = strtext.replace('-', ' ')
    category = Category.objects.get(name=strtext)
    all_products = Product.objects.filter(category=category).order_by('id')
    paginator = Paginator(all_products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shopAll.html', {'products':products, 'category':category})

def shop_brand(request, strtext):
    strtext = strtext.replace('-', ' ')
    brand = Brand.objects.get(name=strtext)
    all_products = Product.objects.filter(brand=brand).order_by('id')
    paginator = Paginator(all_products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shopAll.html', {'products':products, 'brand':brand})

def product(request, slug):
    product = Product.objects.get(slug=slug)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product.html', {'product':product, 'reviews':reviews})

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = 'New Contact Form Submission'
        message_content = f'Name: {full_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['naved.raveed@gmail.com']  #Admin's email

        send_mail(subject, message_content, from_email, recipient_list, fail_silently=False)
        return render(request, 'success.html')
    return render(request, 'contact.html')

def customcandles(request):
    return render(request, 'customcandles.html')

def candlecare(request):
    return render(request, 'candlecare.html', {'product':product})

def submit_review(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            rating = form.cleaned_data['rating']
            review = form.cleaned_data['userreview']
            productreview = Review(username=username, rating=rating, userreview=review, product=product)
            productreview.save()
            return render(request, 'success.html')
    else:
        form = ReviewForm()
    return render(request, 'product.html', {'product': product})