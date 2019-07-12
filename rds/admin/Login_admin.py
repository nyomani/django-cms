from django.contrib import admin
from rds.models import Login


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    pass
