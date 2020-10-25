from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth


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
    user = auth.get_user(request)
    if request.method == "POST" and 'add_favorites' in request.POST:
        article.favorite.add(user)
        return redirect("art_detail", index = index)
    if request.method == "POST" and 'delete_favorites' in request.POST:
        article.favorite.remove(user)
        return redirect("art_detail", index = index)
    else:
        if user in  article.favorite.all():
            in_favorite = True
        else:
            in_favorite = False
        article = Article.objects.get(pk=index)
        return render(request, 'base/article_detail.html', {'article': article,'in_favorite':in_favorite})


def favorites(request):
    user = auth.get_user(request)
    fav = Article.objects.filter(favorite__pk=user.pk)
    paginator = Paginator(fav, 2)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'base/favorites.html', {'articles': page_obj})
