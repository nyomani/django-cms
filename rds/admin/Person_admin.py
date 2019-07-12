from django.contrib import admin
from rds.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
