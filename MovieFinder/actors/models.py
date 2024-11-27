from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Actor(models.Model):
    full_name = models.CharField(
        max_length=30,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    nationality = models.CharField(
        max_length=30,
    )


