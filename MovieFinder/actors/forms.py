from django import forms

from MovieFinder.actors.models import Actor


class ActorBaseForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

        labels = {
            'full_name': 'Name',
            'all_movies': 'Movies',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter an actor name...'}),
            'photo': forms.TextInput(attrs={'placeholder': 'Put a photo...'}),
            'age': forms.TextInput(attrs={'placeholder': 'Write the age...'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter the country...'}),
        }


class ActorCreate(ActorBaseForm):
    pass


class ActorEdit(ActorBaseForm):
    pass


class ActorDelete(ActorBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['disabled'] = True


class SearchForm(forms.Form):
    actor_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'width:300px;padding:10px;font-size:16px;border:1px solid #ccc;border-radius:5px;outline:none;box-shadow:2px 2px 5px rgba(0,0,0,0.1);',
            'placeholder': 'Search by name...'
        }),
        label=''
    )