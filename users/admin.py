from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Custom fields", {"fields": ("avatar", "gender")}),)
    list_display = (
        "username", "first_name", "last_name", "email", "is_active", "language", "currency", "super_host", "is_staff",
        "is_superuser")
    list_filter = UserAdmin.list_filter + ("super_host",)
