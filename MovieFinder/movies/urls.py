from django.urls import path, include

from MovieFinder.movies import views
from MovieFinder.movies.views import MovieRatingView

urlpatterns = [
    path('create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('catalogue/', views.Catalogue.as_view(), name='movie-catalogue'),
    path('<int:pk>/', include([
        path('edit/', views.MovieEditView.as_view(), name='movie-edit'),
        path('delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
        path('rate/', MovieRatingView.as_view(), name='rate_movie'),
        path('details/comment/', views.CommentCreateView.as_view(), name='comment-movie'),
        path('details/', views.MovieDetailsView.as_view(), name='movie-details'),
    ])),
]

