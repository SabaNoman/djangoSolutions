from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    path('shopAll/', views.shop_all, name='shop_all'),
    path('shopAll/category/<str:strtext>', views.shop_category, name='shopcategory'),
    path('shopAll/brand/<str:strtext>', views.shop_brand, name='shopbrand'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('customcandles/', views.customcandles, name='custom_candles'),
    path('candlecare/', views.candlecare, name='candle_care'), 
    path('submit/<int:pk>/', views.submit_review, name='submit_review'),   
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)