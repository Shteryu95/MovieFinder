from django.urls import path

from MovieFinder.common.views import HomePage
from MovieFinder.movies.views import delete_comment

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('comment/<int:comment_pk>/delete/', delete_comment, name='comment_delete'),
]