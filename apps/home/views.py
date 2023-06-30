from django.shortcuts import render
from django.views import View


class IndexShopView(View):
    def get(self, request):
        context = {'data': [
            {'name': 'FOUR CHEESE PIZZA',
             'discount': None,
             'price_before': 14.00,
             'id': 1,
             'url': 'products/pizza-4cheese.jpg'},
            {'name': 'Prosciutto Funghi Pizza',
             'discount': None,
             'price_before': 15.00,
             'id': 2,
             'url': 'products/pizza-proshuto.jpg'},
            {'name': 'BEEF TARTARE WITH PARMESAN MOUSSE',
             'discount': None,
             'price_before': 10.00,
             'id': 3,
             'url': 'products/beeftartar.jpg'},
            {'name': 'MAROCHINO',
             'discount': None,
             'price_before': 4.00,
             'id': 4,
             'url': 'products/marochino.jpg'},



        ]}

        return render(request, 'home/index.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')


class ShippingView(View):
    def get(self, request):
        return render(request, 'home/shipping.html')
