from django.shortcuts import render, redirect

from article.models import Article, Comment
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')
    articles = Article.objects.order_by('-created_at')
    paginator = Paginator(articles, 3)
    page_obj = paginator.get_page(page)

    return render(request, 'index.html', {'articles' : page_obj})

def show(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article_id = pk)

    return render(request, 'show.html', {'article' : article, 'comments' : comments})

def create(request):
    if request.method == 'POST':
        article = Article()
        article.author = request.user
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article:show', pk=article.pk)
    else:
        return render(request, 'new.html')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'edit.html', {"article" : article})

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()

    return redirect('article:show', pk=article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')


# 여기 pk는 article id.
def create_comment(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        comment = Comment()
        comment.article = article
        comment.content = request.POST['content']
        comment.author = request.user
        comment.save()
    return redirect('article:show', pk=pk)
