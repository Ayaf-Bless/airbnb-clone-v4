from django.db import models
from django_countries.fields import CountryField
# own imports
from core import models as core_model
from users import models as users_model


class AbstractItem(core_model.Core):
    """abstract item"""
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Photo(core_model.Core):
    caption = models.CharField(max_length=140)
    file = models.ImageField()
    room = models.ForeignKey(to="Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class Room(core_model.Core):
    """ Rooms model """
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(to=users_model.User, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(to=RoomType, on_delete=models.SET_NULL, null=True, related_name="rooms")
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
