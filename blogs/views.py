from django.shortcuts import render
from blogs.models import Post

def home(request):
    data = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', data)

def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})
