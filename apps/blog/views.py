from django.shortcuts import render
from django.views import View
from .models import Article

# class BlogView(View):
#     def get(self, request):
#         return render(request, 'blog/blog.html')

class BlogView(View):
    def get(self, request):
        # articles = Article.objects.all()
        articles = Article.objects.order_by('-publication_date')
        return render(request, 'blog/blog.html', {"articles": articles})


class BlogSingleView(View):
    def get(self, request, article_id=1):
        data = Article.objects.get(id=article_id)
        return render(request, 'blog/blog-single.html', {"article": data})
