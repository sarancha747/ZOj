from django.contrib import admin
from .models import Article, Tags, ArticleComments, Section

# Register your models here.

admin.site.register(Article)
admin.site.register(Tags)
admin.site.register(ArticleComments)
admin.site.register(Section)