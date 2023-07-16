from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Article, Comment


class BlogView(View):
    """Отображение всех статей (сортированы по дате написания)"""
    def get(self, request):
        articles = Article.objects.order_by('-publication_date')
        return render(request, 'blog/blog.html', {"articles": articles})


class BlogSingleView(View):
    """Отображение отдельных статей"""
    def get(self, request, article_id=1):
        data = Article.objects.get(id=article_id)
        comments = Comment.objects.filter(article=data)
        return render(request, 'blog/blog-single.html', {"article": data, "comments": comments})

    def post(self, request, article_id=1):
        """Создание комментария к статье"""
        if request.user.is_authenticated:
            data = Article.objects.get(id=article_id)
            content = request.POST.get('content')
            if content:
                comment = Comment.objects.create(article=data, user=request.user, content=content)
                comment.save()
            return redirect('blog:blogsingle', article_id=article_id)
        return redirect('login:login')


class DeleteCommentView(View):
    """Удаление комментариев к статьям"""
    def get(self, request, comment_id):
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, id=comment_id)
            if comment.user == request.user:
                comment.delete()
        return redirect('blog:blogsingle', article_id=comment.article.id)
