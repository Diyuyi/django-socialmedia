# profiles/urls.py
from django.urls import path
from .views import ProfileDetailView, ProfileCreateView, ProfileUpdateView

app_name = 'profiles'

urlpatterns = [
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
]
