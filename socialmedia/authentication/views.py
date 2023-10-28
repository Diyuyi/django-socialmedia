from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,CustomAuthenticationForm,ChangePasswordForm
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.shortcuts import redirect,render


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

class LoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'authentication/login.html'
    def form_valid(self, form):
        user = form.get_user()        
        if user.is_authenticated:
            context = {'user': user, }            
            return render(self.request, 'index.html', context)
        
        return super().form_valid(form)

class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/change_password.html'
    def form_valid(self, form):
        messages.success(self.request, 'Thay đổi mật khẩu thành công.')  # Thông báo thành công
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Thay đổi mật khẩu thất bại.')  # Thông báo không thành công
        return super().form_invalid(form)