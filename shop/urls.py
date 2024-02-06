from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    path('shopAll/', views.shop_all, name='shop_all'),
    path('product/<int:pk>', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('customcandles/', views.customcandles, name='custom_candles'),
    path('candlecare/', views.candlecare, name='candle_care'),
    path('category/<str:strtext>', views.brand, name='brand'),
    path('brand/<str:strtext>', views.candle, name='category'),
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)