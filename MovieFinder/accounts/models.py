from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from MovieFinder.accounts.managers import CustomUserManager
from MovieFinder.accounts.validators import UsernameValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=15,
        unique=True,
        validators=[UsernameValidator()],
    )

    email = models.EmailField(
        unique=True
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', ]

    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=CASCADE,
        primary_key=True
    )

    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
    )

    profile_photo = models.ImageField(upload_to='', null=True, blank=True, default='no photo.png')

