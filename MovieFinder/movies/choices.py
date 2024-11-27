from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = 'Action', 'Action'
    COMEDY = 'Comedy', 'Comedy'
    HORROR = 'Horror', 'Horror'
    DRAMA = 'Drama', 'Drama'
    FANTASY = 'Fantasy', 'Fantasy'
    THRILLER = 'Thriller', 'Thriller'
    BIOGRAPHY = 'Biography', 'Biography'
    ANIME = 'Anime', 'Anime'
    MUSICAL = 'Musical', 'Musical'
    MISTERY = 'Mistery', 'Mistery'
    CRIME = 'Crime', 'Crime'
    ADVENTURE = 'Adventure', 'Adventure'
    DOCUMENTARY = 'Documentary', 'Documentary'
    SCI_FI = 'Sci-fi', 'Sci-Fi'
    SPORT = 'Sport', 'Sport'
    WESTERN = 'Western', 'Western'
