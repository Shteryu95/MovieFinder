from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView

from MovieFinder.common.forms import RatingForm
from MovieFinder.common.models import Rating, Comment
from MovieFinder.movies.forms import CreateMovie, EditMovie, DeleteMovie, SearchForm, CommentForm
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
    model = Movie
    form_class = DeleteMovie
    template_name = 'movie-delete.html'
    success_url = reverse_lazy('movie-catalogue')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class MovieDetailsView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'movie-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['user_rating'] = Rating.objects.filter(
                to_movie=self.object.pk,
                user=self.request.user
            ).first()
        context['rating_form'] = RatingForm()
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'movie-details.html'

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['pk'])

        form.instance.movie = movie
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'pk': self.object.movie.id})


class MovieRatingView(LoginRequiredMixin, FormView):
    form_class = RatingForm

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['pk'])
        rating_value = form.cleaned_data['rating']

        rating, created = Rating.objects.update_or_create(
            user=self.request.user,
            to_movie=movie,
            defaults={'rating': rating_value}
        )

        return redirect('movie-details', pk=movie.pk)


class Catalogue(ListView):
    model = Movie
    context_object_name = 'all_movies'
    template_name = 'catalogue.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name_or_genre = self.request.GET.get('movie_name_or_genre')

        if search_name_or_genre:
            queryset = queryset.filter(
                Q(name__icontains=search_name_or_genre) | Q(genre__icontains=search_name_or_genre))

        return queryset


