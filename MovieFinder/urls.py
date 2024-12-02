from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MovieFinder.common.urls')),
    path('accounts/', include('MovieFinder.accounts.urls')),
    path('movie/', include('MovieFinder.movies.urls')),
    path('actors/', include('MovieFinder.actors.urls')),
]
