from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cart, Wishlist
from apps.shop.models import Product
from django.db.models import F, DecimalField, Sum, Case, When
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, WishlistSerializer


class CartView(View):
    """Отображение корзины товаров"""

    def get(self, request):
        if request.user.is_authenticated:
            user_cart = Cart.objects.filter(user=request.user).select_related('product')

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
        return redirect('login:login')


class CartViewBuy(View):
    """Функционал добавления товара в корзину (с переходом на страницу корзины товаров)"""

    def get(self, request, product_id):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            user = get_object_or_404(User, id=request.user.id)

            quantity = int(request.GET.get('quantity', 1))

            cart_items = Cart.objects.filter(user=user, product=product)
            if cart_items:
                cart_item = cart_items[0]
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item = Cart(user=user, product=product, quantity=quantity)
                cart_item.save()

            return redirect('cart:cart')
        return redirect('login:login')


class CartViewAdd(View):
    """Добавление в корзину товаров (без перехода на страницу корзины товаров)"""

    def get(self, request, product_id):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            user = get_object_or_404(User, id=request.user.id)
            cart_items = Cart.objects.filter(user=user, product=product)
            if cart_items:
                cart_item = cart_items[0]
                cart_item.quantity += 1
            else:
                cart_item = Cart(user=user, product=product)
            cart_item.save()
            data = request.GET.urlencode()
            return redirect(reverse('shop:shop') + "?" + data)
        return redirect('login:login')


class CartViewDel(View):
    """Удаление товаров из корзины"""

    def get(self, request, product_id):
        cart_item = Cart.objects.get(user=request.user, product__id=product_id)
        cart_item.delete()
        return redirect('cart:cart')


class WishlistView(View):
    """Отображение списки избранных товаров"""

    def get(self, request):
        if request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user=request.user)
            return render(request, "cart/wishlist.html", {'wishlist': wishlist})
        return redirect('login:login')

    def post(self, request, id):
        # Логика для добавления товара в список желаний
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=id)
            wishlist_item = Wishlist.objects.filter(user=request.user, product=product)

            if wishlist_item.exists():
                return redirect('shop:shop')
            else:
                wishlist_item = Wishlist(user=request.user, product=product)
                wishlist_item.save()
                return redirect('shop:shop')
        return redirect('login:login')

    def delete(self, request, id):
        # Логика для удаления товара из списка желаний
        product = get_object_or_404(Product, id=id)
        wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
        wishlist_item.delete()
        return redirect('cart:wishlist')

    def dispatch(self, request, *args, **kwargs):
        if 'method' in kwargs:
            if kwargs['method'] == 'remove':
                return self.delete(request, id=kwargs['id'])
            elif kwargs['method'] == 'add':
                return self.post(request, id=kwargs['id'])
        return super().dispatch(request, *args, **kwargs)


# API

class CartViewAPI(viewsets.ModelViewSet):
    """API для корзины товаров"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        cart_items = self.get_queryset().filter(product__id=request.data.get('product'))
        if cart_items:
            cart_item = cart_items[0]
            if request.data.get('quantity'):
                cart_item.quantity += int(request.data.get('quantity'))
            else:
                cart_item.quantity += 1
        else:
            product = get_object_or_404(Product, id=request.data.get('product'))
            if request.data.get('quantity'):
                cart_item = Cart(user=request.user, product=product, quantity=request.data.get('quantity'))
            else:
                cart_item = Cart(user=request.user, product=product)
        cart_item.save()
        return response.Response({'message': 'Product added to cart'}, status=201)

    def update(self, request, *args, **kwargs):
        cart_item = get_object_or_404(Cart, id=kwargs['pk'])
        if request.data.get('quantity'):
            cart_item.quantity = request.data['quantity']
        if request.data.get('product'):
            product = get_object_or_404(Product, id=request.data['product'])
            cart_item.product = product
        cart_item.save()
        return response.Response({'message': 'Product change to cart'}, status=201)

    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_queryset().get(id=kwargs['pk'])
        cart_item.delete()
        return response.Response({'message': 'Product delete from cart'}, status=201)


class WishlistViewAPI(viewsets.ModelViewSet):
    """API для списка избранных товаров"""
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        wishlist_items = self.get_queryset().filter(product__id=request.data.get('product'))
        if wishlist_items:
            wishlist_item = wishlist_items[0]
        else:
            product = get_object_or_404(Product, id=request.data.get('product'))
            wishlist_item = Wishlist(user=request.user, product=product)
        wishlist_item.save()
        return response.Response({'message': 'Product added to wishlist'}, status=201)

    def update(self, request, *args, **kwargs):
        wishlist_item = get_object_or_404(Wishlist, id=kwargs['pk'])
        if request.data.get('product'):
            product = get_object_or_404(Product, id=request.data['product'])
            wishlist_item.product = product
        wishlist_item.save()
        return response.Response({'message': 'Product change to wishlist'}, status=201)

    def destroy(self, request, *args, **kwargs):
        wishlist_item = self.get_queryset().get(id=kwargs['pk'])
        wishlist_item.delete()
        return response.Response({'message': 'Product delete from wishlist'}, status=201)
