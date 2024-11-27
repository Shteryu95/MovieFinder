from django import forms

from MovieFinder.common.choices import GenreChoices
from MovieFinder.common.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.RadioSelect(choices=GenreChoices)
        }