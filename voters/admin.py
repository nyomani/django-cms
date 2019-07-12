from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.models import LogEntry
# Register your models here.
from . import models

class RegistrationAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','voting_method','registration_status','voting_status','notes')
    list_display_links = ('first_name','last_name','notes')
    list_filter =('voting_method','registration_status','voting_status','voting_method')
    search_fields = ('person__first_name','person__last_name','person__email')
admin.site.register(LogEntry)
admin.site.register(models.PersonRegistration,RegistrationAdmin)
