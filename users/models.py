from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE,"Female"),
        (GENDER_OTHER, "Other")
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, null=True, blank=True)

