from django.contrib import admin
from rds.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
