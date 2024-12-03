from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MovieFinder.common.urls')),
    path('accounts/', include('MovieFinder.accounts.urls')),
    path('movie/', include('MovieFinder.movies.urls')),
    path('actors/', include('MovieFinder.actors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
