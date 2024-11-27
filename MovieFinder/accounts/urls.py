from django.contrib.auth.views import LogoutView
from django.urls import path, include

from MovieFinder.accounts import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', views.ProfileDetailsView.as_view(), name='profile'),
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]