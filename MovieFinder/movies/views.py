from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from MovieFinder.movies.forms import CreateMovie, EditMovie
from MovieFinder.movies.models import Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = CreateMovie
    success_url = reverse_lazy('home')
    template_name = 'movie-create.html'

    def form_valid(self, form):
        movie = form.save(commit=False)
        movie.user = self.request.user
        return super().form_valid(form)


class MovieEditView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = EditMovie
    template_name = 'movie-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'movie-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


class MovieDeleteView(DeleteView):
    pass


class MovieDetailsView(DetailView):
    model = Movie
    template_name = 'movie-details.html'


class Catalogue(ListView):
    model = Movie
    context_object_name = 'all_movies'
    template_name = 'catalogue.html'
