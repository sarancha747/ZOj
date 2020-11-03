from django.urls import path
from . import views

urlpatterns = [
    path ('', views.start, name = 'start'),
    path ('article/<slug:slug>/', views.art_detail, name = 'art_detail'),
    path ('favorites/', views.favorites, name = 'favorites'),
    path ('science/', views.science, name = 'science'),
    path('technology/', views.technology, name='technology')
]

