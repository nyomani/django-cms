from django.contrib import admin
from rds.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass
