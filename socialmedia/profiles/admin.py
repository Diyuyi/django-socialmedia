# profiles/admin.py
from django.contrib import admin
from .models import Profile
from .forms import ProfileForm

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm  # Sử dụng ProfileForm khi thêm hoặc chỉnh sửa profiles trong admin site
    list_display = ('user', 'bio', 'phone_number')  # Các trường sẽ được hiển thị trong danh sách profiles
    search_fields = ('user__username', 'bio', 'phone_number')  # Các trường mà admin có thể tìm kiếm

admin.site.register(Profile, ProfileAdmin)  # Đăng ký model Profile với cấu hình admin đã tạo
