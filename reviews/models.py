from typing import Any

from django.db import models
from core import models as core_models


class Review(core_models.Core):
    """Review model definitions"""
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.room} - {self.review}"

    def get_avg(self):
        avg = (self.accuracy
               + self.communication +
               self.cleanliness +
               self.location +
               self.check_in +
               self.value) / 6
        return round(avg, 2)
