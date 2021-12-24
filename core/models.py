from django.db import models


class Core(models.Model):
    """Time stamped model"""
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        abstract = True
