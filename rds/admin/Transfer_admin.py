from django.contrib import admin
from rds.models import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass
