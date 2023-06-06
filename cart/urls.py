from django.urls import path
from .views import CartView, WishlistView

app_name = "cart"

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('wishlist', WishlistView.as_view(), name='wishlist')

]