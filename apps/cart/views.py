from django.shortcuts import render
from django.views import View
from .models import Cart, Product
from django.db.models import F
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

class CartView(View):
    # def get(self, request):
    #     return render(request, 'cart/cart.html')

    def get(self, request):
        cart = Cart.objects.filter(user=request.user).annotate(
            total_price=F('product__price') * F('quantity')
        )

        return render(request, 'cart/cart.html', {"data": cart})

class CartViewBuy(View):
        def get(self, request, product_id):
            product = get_object_or_404(Product, id=product_id)
            user = get_object_or_404(User, id=request.user.id)
            cart_items = Cart.objects.filter(user=user, product=product)
            if cart_items:
                cart_item = cart_items[0]
                cart_item.quantity += 1
            else:
                cart_item = Cart(user=user, product=product)
            cart_item.save()
            return redirect('cart:cart')


class CartViewAdd(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(User, id=request.user.id)
        cart_items = Cart.objects.filter(user=user, product=product)
        if cart_items:
            cart_item = cart_items[0]
            cart_item.quantity += 1
        else:
            cart_item = Cart(user=user, product=product)
        cart_item.save()
        return redirect('shop:shop')


class WishlistView(View):
    def get(self, request):
        return render(request, 'cart/wishlist.html')
