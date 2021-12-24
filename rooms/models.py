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
    pass


class Amenity(AbstractItem):
    pass


class HouseRule(AbstractItem):
    pass


class Facility(AbstractItem):
    pass


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
    host = models.ForeignKey(to=users_model.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(to=RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
