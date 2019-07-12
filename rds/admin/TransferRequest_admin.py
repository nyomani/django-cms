from django.contrib import admin
from rds.models import Transferrequest


@admin.register(Transferrequest)
class TransferrequestAdmin(admin.ModelAdmin):
    pass
