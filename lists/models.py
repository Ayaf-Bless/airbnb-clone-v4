from django.db import models
from core import models as core_models


class List(core_models.Core):
    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="lists")
    rooms = models.ManyToManyField("rooms.room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "number of rooms"
