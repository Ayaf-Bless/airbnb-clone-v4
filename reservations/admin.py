from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = ("room", "status", "guest", "check_in", "check_out", "in_progress", "is_finished")
    list_filter = ("status",)
