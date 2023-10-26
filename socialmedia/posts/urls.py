from django.urls import path
from . import views

urlpatterns = [
    path('<str:page>/', views.index, name='home'),
    path('friend/', views.friend, name='friend'),
    path('group/', views.group, name='group'),
]