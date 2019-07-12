from django.contrib import admin
from rds.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
