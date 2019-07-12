from django.contrib import admin
from rds.models import Tally


@admin.register(Tally)
class TallyAdmin(admin.ModelAdmin):
    pass
