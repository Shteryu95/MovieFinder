from django.views.generic import TemplateView

from MovieFinder.movies.models import Movie


class HomePage(TemplateView):
    model = Movie
    template_name = 'home-page.html'
