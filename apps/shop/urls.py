from django.urls import path
from .views import ShopView, ProductSingleView
from apps.cart.views import CartViewBuy, CartViewAdd

app_name = "shop"

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('product/<int:product_id>', ProductSingleView.as_view(), name='productsingle'),
    path('product/', ProductSingleView.as_view(), name='productsingle'),
    path('buy/<int:product_id>', CartViewBuy.as_view(), name='buy'),
    path('add/<int:product_id>', CartViewAdd.as_view(), name='add'),

]
