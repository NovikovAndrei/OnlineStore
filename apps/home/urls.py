from django.urls import path
from .views import IndexShopView, AboutView, ContactView, ShippingView

app_name = "home"

urlpatterns = [
    path('', IndexShopView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shipping/', ShippingView.as_view(), name='shipping'),
]