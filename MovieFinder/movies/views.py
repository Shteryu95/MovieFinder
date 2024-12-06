from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from MovieFinder.common.forms import RatingForm
from MovieFinder.common.models import Rating
from MovieFinder.movies.forms import CreateMovie, EditMovie, DeleteMovie, SearchForm, CommentForm
from MovieFinder.movies.models import Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = CreateMovie
    success_url = reverse_lazy('movie-catalogue')
    template_name = 'movie-create.html'

    def form_valid(self, form):
        movie = form.save(commit=False)
        movie.user = self.request.user
        messages.success(self.request, "Your movie has been submitted and is awaiting approval.")
        if movie.user.is_staff:
            movie.approved = True

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
        context['actors'] = self.object.movie_actors.all
        return context

    def post(self, request, *args, **kwargs):
        movie = self.get_object()
        comment_form = CommentForm(request.POST)
        rating_form = RatingForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movie-details', pk=movie.pk)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.to_movie = movie
            rating.user = request.user
            rating.save()
            return redirect('movie-details', pk=movie.pk)

        return self.get(request, *args, **kwargs)


class Catalogue(ListView):
    model = Movie
    context_object_name = 'all_movies'
    template_name = 'catalogue.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name_or_genre = self.request.GET.get('movie_name_or_genre')

        if not self.request.user.has_perm('movies.approve_movies'):
            queryset = queryset.filter(approved=True)

        if search_name_or_genre:
            queryset = queryset.filter(
                Q(name__icontains=search_name_or_genre) | Q(genre__icontains=search_name_or_genre))

        return queryset


def approve_movies(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.approved = True
    movie.save()

    return redirect(request.META.get('HTTP_REFERER'))
