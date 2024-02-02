from django.shortcuts import render
from .models import Article


def get_index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def get_info(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'blog/article_info.html', {'article': article})


def get_main(request):
    return render(request, 'blog/main.html')
