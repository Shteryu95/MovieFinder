from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator:
    def __init__(self, username=None):
        self.username = username

    def __call__(self, value):
        if not value.isalnum():
            raise ValidationError("Your username must contain only letters and digits!")