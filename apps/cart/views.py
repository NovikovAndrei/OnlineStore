from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cart, Product
from django.db.models import F, OuterRef, Subquery, DecimalField, ExpressionWrapper, Sum, Case, When
from django.contrib.auth.models import User
from django.utils import timezone


class CartView(View):
    def get(self, request):
        user_cart = Cart.objects.filter(user=request.user). \
            select_related('product')

        total_discount = Case(When(product__discount__value__gte=0,
                                   product__discount__date_begin__lte=timezone.now(),
                                   product__discount__date_end__gte=timezone.now(),
                                   then=F('total_price') * F('product__discount__value') / 100),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
        )
        cart = user_cart.annotate(
            total_price=F('product__price') * F('quantity'),
            total_discount=total_discount,
            total_price_with_discount=F('total_price') - F('total_discount'),
        )

        sum_data = cart.aggregate(sum_price=Sum('total_price'),
                                  sum_discount=Sum('total_discount'),
                                  sum_price_with_discount=Sum('total_price_with_discount'))

        context = {"data": cart}
        context.update(sum_data)

        return render(request, 'cart/cart.html', context)

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

class CartViewDel(View):
  def get(self, request, product_id):

      cart_item = Cart.objects.get(user=request.user, product__id=product_id)
      cart_item.delete()
      return redirect('cart:cart')


class WishlistView(View):
    def get(self, request):
        return render(request, 'cart/wishlist.html')
