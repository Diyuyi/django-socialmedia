from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home1'),
    path('posts/<str:page>/', index, name='home'),
    path('upload_post/', AddPostView.as_view(), name='upload_post'),
]