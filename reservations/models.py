from django.db import models
from core import models as core_models


class Reservation(core_models.Core):
    STATUS_CONFIRMED = "confirmed"
    STATUS_PENDING = "pending"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_PENDING, "Pending"),
        (STATUS_CANCELED, "Canceled")
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(to="rooms.Room", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.check_in}"
