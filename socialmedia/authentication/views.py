# authentication/views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ChangePasswordForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, render
from profiles.models import Profile  # Import the Profile model

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # This will create the user
        profile_pic_path = 'cover_photos/logotdc.jpg'  # Replace with the actual path to your static image
        Profile.objects.create(user=self.object, profile_pic=profile_pic_path)  #
        return response  # Return the response object to continue the no

# class LoginView(LoginView):
#     form_class = CustomAuthenticationForm
#     template_name = 'authentication/login.html'

#     def form_valid(self, form):
#         response = super().form_valid(form)  # This will log the user in
#         user_profile_url = reverse('profiles:profile', kwargs={'pk': self.request.user.pk})
#         return redirect(user_profile_url)  # Redirect to user's profile page

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