from django.urls import path
from . import views

urlpatterns = [
    path ('', views.start, name = 'start'),
    path ('article/<int:index>/', views.art_detail, name = 'art_detail'),
    path ('favorites/', views.favorites, name = 'favorites')
]

