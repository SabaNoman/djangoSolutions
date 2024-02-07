from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import shop_all

urlpatterns = [
    path('', views.homepage, name='home'),
    path('shopAll/', views.shop_all, name='shop_all'),
    path('shop-all/', shop_all, name='shop_all'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('customcandles/', views.customcandles, name='custom_candles'),
    path('candlecare/', views.candlecare, name='candle_care'),
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)