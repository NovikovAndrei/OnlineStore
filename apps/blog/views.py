from django.shortcuts import render, redirect
from django.views import View
from .models import Article, Comment


class BlogView(View):
    def get(self, request):
        # articles = Article.objects.all()
        articles = Article.objects.order_by('-publication_date')
        return render(request, 'blog/blog.html', {"articles": articles})


class BlogSingleView(View):
    def get(self, request, article_id=1):
        data = Article.objects.get(id=article_id)
        comments = Comment.objects.filter(article=data)
        return render(request, 'blog/blog-single.html', {"article": data, "comments": comments})

    def post(self, request, article_id=1):
        data = Article.objects.get(id=article_id)
        content = request.POST.get('content')
        if content:
            comment = Comment.objects.create(article=data, user=request.user, content=content)
            comment.save()
        return redirect('blog:blogsingle', article_id=article_id)