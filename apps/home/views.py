from django.shortcuts import render
from django.views import View
from .models import Testimony
import codecs

class IndexShopView(View):
    def get(self, request):
        testimonies = Testimony.objects.all()
        context = {
            'data': [
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
            ],
            'testimonies': testimonies
        }

        return render(request, 'home/index.html', context)

class AboutView(View):
    def get(self, request):
        testimonies = Testimony.objects.all()
        context = {
            'testimonies': testimonies
        }
        return render(request, 'home/about.html', context)

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')


class ShippingView(View):
    def get(self, request):
        return render(request, 'home/shipping.html')

class ReturnsView(View):
    def get(self, request):
        return render(request, 'home/returns.html')

class TermsConditionsView(View):
    def get(self, request):
        return render(request, 'home/termsconditions.html')

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'home/privacy-policy.html')

class FAQView(View):
    def get(self, request):
        return render(request, 'home/faq.html')


class ReadmeView(View):
    def get(self, request):
        with codecs.open('readme.md', 'r', encoding='utf-8') as file:
            readme_content = file.read()

        readme_lines = readme_content.split('\n')
        readme_html = '<br><br>'.join(readme_lines)

        return render(request, 'home/readme.html', {'readme_content': readme_html})


