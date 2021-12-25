from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class AdminReservation(admin.ModelAdmin):
    pass
