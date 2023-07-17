from django.contrib import admin
from django.urls import path, include
from apps.cart.urls import router as cart_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('cart/', include('apps.cart.urls')),
    path('shop/', include('apps.shop.urls')),
    path('checkout/', include('apps.checkout.urls')),
    path('blog/', include('apps.blog.urls')),
    path('login/', include('apps.login.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include(cart_router.urls)),
]
