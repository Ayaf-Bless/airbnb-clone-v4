from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import hashlib
from django.conf import settings


class User(AbstractUser):
    """User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_FRENCH = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_FRENCH, "French"), (LANGUAGE_ENGLISH, "English"))

    CURRENCY_USD = "usd"
    CURRENCY_EU = "eu"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_EU, "EU"))

    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_FRENCH
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=5, blank=True, default=CURRENCY_USD
    )
    super_host = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is not False:
            token = uuid.uuid4().hex[:20]
            self.email_token = hashlib.sha224(b"{token}").hexdigest()
            send_mail(
                'Verify your account',
                f'verify your email. this is your secret: {token}',
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )

        return
