from django.contrib import admin
from rds.models import Registrationlog


@admin.register(Registrationlog)
class RegistrationlogAdmin(admin.ModelAdmin):
    pass
