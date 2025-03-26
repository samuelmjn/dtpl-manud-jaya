from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    pass

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)

    context = {
        'news': news,
    }
    return render(request, 'news/news_detail.html', context)