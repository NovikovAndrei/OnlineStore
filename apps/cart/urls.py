from rest_framework import routers
from django.urls import path
from .views import CartView, WishlistView, CartViewDel, CartViewAPI, WishlistViewAPI

router = routers.DefaultRouter()
router.register(r'cart', CartViewAPI)
router.register(r'wishlist', WishlistViewAPI)

app_name = "cart"

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('del/<int:product_id>', CartViewDel.as_view(), name='del'),
    path('wishlist/remove/<int:id>/', WishlistView.as_view(), {'method': 'remove'}, name='remove_from_wishlist'),
    path('wishlist/add/<int:id>/', WishlistView.as_view(), {'method': 'add'}, name='add_to_wishlist'),

]