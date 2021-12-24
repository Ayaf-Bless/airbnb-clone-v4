from django.db import models


class Core(models.Model):
    """Time stamped model"""
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
