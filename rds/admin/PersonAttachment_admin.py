from django.contrib import admin
from rds.models import Personattachment


@admin.register(Personattachment)
class PersonattachmentAdmin(admin.ModelAdmin):
    pass
