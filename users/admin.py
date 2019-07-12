from django.contrib import admin
from .models import UserProfile
from .types import (
    VoterType,VotingMethod,VotingStatus,
    RegistrationStatus,DisabilityType,
    MaritalStatus,Gender,IdentificationType,
    PendingReason,RejectReason
    )
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('image','email', 'first_name' , 'last_name', 'id_type','identification',
                  'birthPlace','birthDate','address','city','state','zipCode','telp','gender',
                  'marital_status','disability')

class UserAdmin(DjangoUserAdmin):
    add_form = CreateUserForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(UserProfile,UserAdmin)
admin.site.register(DisabilityType)
admin.site.register(VotingMethod)
admin.site.register(VoterType)
admin.site.register(RegistrationStatus)
admin.site.register(VotingStatus)
admin.site.register(MaritalStatus)
admin.site.register(Gender)
admin.site.register(IdentificationType)
admin.site.register(PendingReason)
admin.site.register(RejectReason)
