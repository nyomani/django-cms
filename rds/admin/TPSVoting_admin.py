from django.contrib import admin
from rds.models import Tpsvoting


@admin.register(Tpsvoting)
class TpsvotingAdmin(admin.ModelAdmin):
    pass
