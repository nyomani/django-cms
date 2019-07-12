from cms.extensions import PageExtensionAdmin
from django.contrib import admin
from ppln.page import MetaPage, PageGroup

admin.site.register(MetaPage, PageExtensionAdmin)
admin.site.register(PageGroup)