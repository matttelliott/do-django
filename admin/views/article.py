from django.contrib import admin
from schema.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
