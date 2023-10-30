# friendships/forms.py
from django import forms
from .models import Friendship, Follow

class FriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['user2', 'status']

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ['followee']
