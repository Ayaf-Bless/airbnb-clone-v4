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
                    "host",
                    "count_amenities")
    list_filter = ("host", "country", "city")
    search_fields = ("city", "host__username")
    filter_horizontal = ("amenities",
                         "facilities",
                         "house_rules",)

    ordering = ("name", "city")

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "number of amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
