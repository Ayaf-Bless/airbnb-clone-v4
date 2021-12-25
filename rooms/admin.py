from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "description",
                    "country",
                    "city",
                    "price",
                    "guests",
                    "host",)
    list_filter = ("host", "country", "city")
    search_fields = ("city", "host__username")
    filter_horizontal = ("amenities",
                         "facilities",
                         "house_rules",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
