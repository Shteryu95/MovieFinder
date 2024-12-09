from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class NameValidator:
    def __init__(self, full_name=None):
        self.full_name = full_name

    def __call__(self, value):
        if not re.match(r'^[a-zA-Z ]+$', value):
            raise ValidationError("The full name of the actor must contain only letters and spaces!")

        if len(value.split()) < 2:
            raise ValidationError("Full name must consist of more than one name.")