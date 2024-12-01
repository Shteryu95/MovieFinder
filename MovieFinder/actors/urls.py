from django.urls import path, include

from MovieFinder.actors import views

urlpatterns = [
    path('create/', views.ActorCreateView.as_view(), name='actor-create'),
    path('catalogue/', views.Catalogue.as_view(), name='actor-catalogue'),
    path('<int:pk>/', include([
        path('edit/', views.ActorEditView.as_view(), name='actor-edit'),
        path('delete/', views.ActorDeleteView.as_view(), name='actor-delete'),
        path('details/', views.ActorDetailsView.as_view(), name='actor-details'),
    ])),
]
