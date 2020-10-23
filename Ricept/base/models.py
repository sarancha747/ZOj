from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    body = RichTextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    favorite = models.ManyToManyField(User)


    def __str__(self):
        return self.title



class Author(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    reg_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user_name
