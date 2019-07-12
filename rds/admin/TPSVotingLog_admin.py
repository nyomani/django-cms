from django.contrib import admin
from rds.models import Tpsvotinglog


@admin.register(Tpsvotinglog)
class TpsvotinglogAdmin(admin.ModelAdmin):
    pass
