from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from authentication.models import User

# Create your views here.

def index(request, page):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'page': page,'post_list':post_list})
def home(request):
    post_list = Post.objects.all()
    return render(request, 'index.html',{'post_list':post_list})

# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = "upload_post.html"
#     def form_valid(self, form):
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('upload_post.html')

class AddPostView(View):
    template_name = 'upload_post.html'

    def get(self, request):
        form = PostForm()  # Tạo một mẫu trống để hiển thị
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)  # Truyền dữ liệu từ POST và FILES vào mẫu
        if form.is_valid():
            print("form sucess")
            post = form.save(commit=False)  # Tạo một bài viết nhưng chưa lưu vào cơ sở dữ liệu
            post.user = request.user  # Gán người dùng hiện tại cho bài viết

            post.save()  # Lưu bài viết vào cơ sở dữ liệu   
        return render(request, self.template_name, {'form': form})
