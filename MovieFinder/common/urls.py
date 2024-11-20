from django.urls import path

from MovieFinder.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]