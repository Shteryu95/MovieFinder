from django.urls import path

from MovieFinder.movies import views

urlpatterns = [
    path('create/', views.MovieCreateView.as_view(), name='movie-create')
]