from django.urls import path
from .views import ShopView, ProductSingleView

app_name = "shop"

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('product/', ProductSingleView.as_view(), name='productsingle')
]