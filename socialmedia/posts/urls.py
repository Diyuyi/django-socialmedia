from django.urls import path
from .views import *

urlpatterns = [
    path('posts/<str:page>/', index, name='home'),
    path('upload_post/', AddPostView.as_view(), name='upload_post'),
]