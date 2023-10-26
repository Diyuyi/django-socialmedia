from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def index(request, page):
    return render(request, 'index.html', {'page': page})

def friend(request):
    return render(request, 'friend.html')

def group(request):
    return render(request, 'group.html')