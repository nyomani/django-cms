from . import models
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import AdminSite
from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from import_export.admin import ImportExportModelAdmin
from .models import (
    IconExtension,Party,
    Candidate,Team,Task,TaskType,
    ElectionType
)

class IconExtensionAdmin(PageExtensionAdmin):
    pass

class PartyAdmin(ImportExportModelAdmin):
    list_display = ('party_id','description','image')
    list_display_links = ('party_id','description')
    list_filter =('party_id','description')
    ordering = ('party_id',)
    search_fields = ('party_id','description')

class CandidateAdmin(ImportExportModelAdmin):
    list_display = ('party','election_type','candidate_id','name','vote_count_tps','vote_count_pos','vote_count')
    list_display_links = ('name','vote_count')
    list_filter =('party','election_type')
    ordering = ('party__party_id','candidate_id')
    search_fields = ('party','party__description','name')

class MetaPageAdmin(PageExtensionAdmin):
    pass

admin.site.register(IconExtension, IconExtensionAdmin)
admin.site.register(Party,PartyAdmin)
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Team)
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(ElectionType)

