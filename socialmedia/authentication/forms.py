from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ChangePasswordForm(PasswordChangeForm):
    # old_password = forms.CharField(widget =forms.PasswordInput(attrs= { 'class':'form-control','type':'password'}))
    # new_password1 = forms.CharField(max_length=100,widget = forms.PasswordInput( attrs = { 'class':'form-control' , 'type':'password'}))
    # new_password2 = forms.CharField(max_length=100,widget=  forms.PasswordInput( attrs = { 'class':'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
