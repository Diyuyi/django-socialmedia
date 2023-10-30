from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        # Vô hiệu hóa xác nhận mật khẩu
        password_confirmation_required = False
        # Vô hiệu hóa kiểm tra độ mạnh mật khẩu
        password_validators = []


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
