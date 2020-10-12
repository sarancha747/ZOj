from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator



# Create your views here.
def start(request):
    article = Article.objects.all()
    paginator = Paginator(article, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(article)
    return render(request, 'base/start_page.html', {'articles':page_obj})

def art_detail(request, index):
    article = Article.objects.get(pk=index)
    return render(request, 'base/article_detail.html', {'article': article})


def favorites(request):
    article = Article.objects.all()
    paginator = Paginator(article, 10)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(article)
    return render(request, 'base/favorites.html', {'articles': page_obj})
