from django.contrib import admin
from rds.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
