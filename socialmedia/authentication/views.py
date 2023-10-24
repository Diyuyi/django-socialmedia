from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

class LoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        print('ok')
        return redirect('register')
