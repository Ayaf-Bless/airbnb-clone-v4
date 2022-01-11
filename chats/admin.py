from django.contrib import admin
from . import models


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("__str__", "count_participants","count_messages")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at",)

