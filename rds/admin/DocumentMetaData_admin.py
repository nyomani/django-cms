from django.contrib import admin
from rds.models import Documentmetadata


@admin.register(Documentmetadata)
class DocumentmetadataAdmin(admin.ModelAdmin):
    pass
