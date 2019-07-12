from django.contrib import admin
from rds.models import Personlog


@admin.register(Personlog)
class PersonlogAdmin(admin.ModelAdmin):
    pass
