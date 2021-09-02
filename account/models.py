from django.db import models
from django.db.models import CASCADE


class Profile(models.Model):

    user = models.OneToOneField(
        "auth.User",
        null=False,
        blank=False,
        on_delete=CASCADE
    )

    contact_number = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    house_address = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    postal_code = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    latitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=15
    )

    longitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=15
    )

    preference_tag = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

