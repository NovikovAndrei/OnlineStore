from django.db import models
from django.contrib.auth.models import User
from apps.shop.models import Product


class Cart(models.Model):
   """Модель для козины товаров"""
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user}_{self.product}"


class Wishlist(models.Model):
   """Модель для списка избранных товаров"""
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.user}_{self.product}"
