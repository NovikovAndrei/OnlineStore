from django.urls import path
from .views import CartView, WishlistView, CartViewDel

app_name = "cart"

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('del/<int:product_id>', CartViewDel.as_view(), name='del'),

]