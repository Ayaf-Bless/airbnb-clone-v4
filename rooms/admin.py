from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.RoomType, models.Amenity, models.HouseRule, models.Facility)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "used_by",)

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "description",
                    "country",
                    "city",
                    "price",
                    "guests",
                    "host",
                    "count_amenities",
                    "count_photo",
                    "total_avg"
                    )
    inlines = [PhotoInline]
    raw_id_fields = ("host",)
    list_filter = ("host", "country", "city")
    search_fields = ("city", "host__username")
    filter_horizontal = ("amenities",
                         "facilities",
                         "house_rules",)

    ordering = ("name", "city")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photo(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "number of amenities"


# @admin.register(models.Room)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo admin"""
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50' src={obj.file.url} />")

    get_thumbnail.short_description = "thumbnail"
