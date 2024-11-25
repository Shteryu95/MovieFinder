from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = 'action', 'Action'
    COMEDY = 'comedy', 'Comedy'
    HORROR = 'horror', 'Horror'
    DRAMA = 'drama', 'Drama'
    FANTASY = 'fantasy', 'Fantasy'
    THRILLER = 'thriller', 'Thriller'
    BIOGRAPHY = 'biography', 'Biography'
    ANIME = 'anime', 'Anime'
    MUSICAL = 'musical', 'Musical'
    MISTERY = 'mistery', 'Mistery'
    CRIME = 'crime', 'Crime'
    ADVENTURE = 'adventure', 'Adventure'
    DOCUMENTARY = 'documentary', 'Documentary'
    SCI_FI = 'sci-fi', 'Sci-Fi'
    SPORT = 'sport', 'Sport'
    WESTERN = 'western', 'Western'
