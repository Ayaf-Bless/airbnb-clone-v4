from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birth_date",
                    "language",
                    "currency",
                    "super_host",
                    "login_method"
                )
            },
        ),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "super_host",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_token",
        "login_method"
    )
    list_filter = UserAdmin.list_filter + ("super_host",)
