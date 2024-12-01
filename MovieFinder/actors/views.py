from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from MovieFinder.actors.forms import ActorCreate, ActorEdit, ActorDelete
from MovieFinder.actors.models import Actor
from MovieFinder.actors.forms import SearchForm


class ActorCreateView(LoginRequiredMixin, CreateView):
    model = Actor
    form_class = ActorCreate
    success_url = reverse_lazy('home')
    template_name = 'actor-create.html'


class ActorEditView(LoginRequiredMixin, UpdateView):
    model = Actor
    form_class = ActorEdit
    template_name = 'actor-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'actor-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


class ActorDeleteView(DeleteView):
    model = Actor
    form_class = ActorDelete
    template_name = 'actor-delete.html'
    success_url = reverse_lazy('')

    def get_initial(self):
        return self.get_object().__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class ActorDetailsView(LoginRequiredMixin, DetailView):
    model = Actor
    template_name = 'actor-details.html'

    def get_context_data(self, **kwargs):
        # Get the base context
        context = super().get_context_data(**kwargs)
        # Add the related actors to the context
        context['movies'] = self.object.all_movies  # Access related actors
        return context


class Catalogue(ListView):
    model = Actor
    context_object_name = 'all_actors'
    template_name = 'actor-catalogue.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('full_name')
        search_full_name = self.request.GET.get('actor_name')

        if search_full_name:
            queryset = queryset.filter(
                full_name__icontains=search_full_name)

        return queryset
