from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    html_title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.CharField(max_length=150)
    html_description = models.CharField(max_length=150)
    body = RichTextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    tag = models.ManyToManyField(Tags)
    favorite = models.ManyToManyField(User)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class ArticleComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commentAuthor')
    post = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=1000)

