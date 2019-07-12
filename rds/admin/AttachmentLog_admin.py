from django.contrib import admin
from rds.models import Attachmentlog


@admin.register(Attachmentlog)
class AttachmentlogAdmin(admin.ModelAdmin):
    pass
