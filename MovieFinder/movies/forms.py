from django import forms

from MovieFinder.movies.models import Movie


class MovieBaseForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['user', ]

        labels = {
            'name': 'Movie name',
            'released_date': 'Released date',
            'genre': 'Genre',
            'poster': 'Movie poster',
            'awards': 'Awards won',
            'resume': 'Short summary',
        }

        widgets = {
            'released_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateMovie(MovieBaseForm):
    pass


class EditMovie(MovieBaseForm):
    pass


class DeleteMovie(MovieBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = True
