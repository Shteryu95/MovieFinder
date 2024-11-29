from django import forms

from MovieFinder.common.models import Comment
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
            self.fields[field_name].widget.attrs['disabled'] = True


class SearchForm(forms.Form):
    movie_name_or_genre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'width:300px;padding:10px;font-size:16px;border:1px solid #ccc;border-radius:5px;outline:none;box-shadow:2px 2px 5px rgba(0,0,0,0.1);',
            'placeholder': 'Search by title or genre...'
        }),
        label=''
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Enter your comment here...',
                'class': 'comment-input',
                'style': 'width: 400px; max-width: 100%;'
            }),
        }
        labels = {
            'text': '',
        }