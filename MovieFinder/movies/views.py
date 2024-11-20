from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from MovieFinder.movies.forms import CreateMovie
from MovieFinder.movies.models import Movie


class MovieCreateView(CreateView):
    model = Movie
    form_class = CreateMovie
    success_url = reverse_lazy('home')
    template_name = 'movie-create.html'

    def form_valid(self, form):
        movie = form.save(commit=False)
        movie.user = self.request.user
        return super().form_valid(form)


class Catalogue(ListView):
    model = Movie
    context_object_name = 'all_movies'
    template_name = 'catalogue.html'
