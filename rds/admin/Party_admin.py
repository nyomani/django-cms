from django.contrib import admin
from rds.models import Party


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    pass
