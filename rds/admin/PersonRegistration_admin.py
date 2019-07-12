from django.contrib import admin
from rds.models import Personregistration


@admin.register(Personregistration)
class PersonregistrationAdmin(admin.ModelAdmin):
    pass
