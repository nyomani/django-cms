from django.contrib import admin
from rds.models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass
