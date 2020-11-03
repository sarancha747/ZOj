from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
from django.db.models import Q


# Create your views here.
def start(request):
    tech_article = Article.objects.filter(section__name__contains='Technology').order_by('-creation_date')[:3]
    sci_article = Article.objects.filter(section__name__contains='Science').order_by('-creation_date')[:3]
    return render(request, 'base/start_page.html', {'tech_article': tech_article, 'sci_article':sci_article})


def art_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    user = auth.get_user(request)
    if request.method == "POST" and 'add_favorites' in request.POST:
        article.favorite.add(user)
        return redirect("art_detail", slug=slug)
    if request.method == "POST" and 'delete_favorites' in request.POST:
        article.favorite.remove(user)
        return redirect("art_detail", slug=slug)
    else:
        if user in article.favorite.all():
            in_favorite = True
        else:
            in_favorite = False
        # article = Article.objects.get(pk=index)
        return render(request, 'base/article_detail.html', {'article': article, 'in_favorite': in_favorite})


def favorites(request):
    user = auth.get_user(request)
    fav = Article.objects.filter(favorite__pk=user.pk)
    paginator = Paginator(fav, 20)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    science = 'Science'
    technology = 'Technology'
    return render(request, 'base/favorites.html', {'articles': page_obj, 'science': science, 'technology': technology})


def science(request):
    search_query = request.GET.get('search', '')
    if search_query:
        article = Article.objects.filter((Q(title__icontains=search_query) | Q(body__icontains=search_query)) & Q(section__name__contains='Science')).order_by('-creation_date')
    else:
        article = Article.objects.filter(section__name__contains='Science').order_by('-creation_date')

    paginator = Paginator(article, 20)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(article)
    return render(request, 'base/science.html', {'articles': page_obj})


def technology(request):
    search_query = request.GET.get('search', '')
    if search_query:
        article = Article.objects.filter((Q(title__icontains=search_query) | Q(body__icontains=search_query)) & Q(section__name__contains='Technology')).order_by('-creation_date')
    else:
        article = Article.objects.filter(section__name__contains='Technology').order_by('-creation_date')

    paginator = Paginator(article, 20)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(article)
    return render(request, 'base/technology.html', {'articles': page_obj})
