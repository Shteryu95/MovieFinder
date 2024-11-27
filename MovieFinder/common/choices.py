from django.db import models


class GenreChoices(models.TextChoices):
    ONE_STAR = '1', '1 star'
    TWO_STARS = '2', '2 stars'
    THREE_STARS = '3', '3 stars'
    FOUR_STARS = '4', '4 stars'
    FIVE_STARS = '5', '5 stars'
