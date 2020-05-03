from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Author, Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by('-created_date')[:10]
    posts = [{ 'title': p.title, 
                'tag': p.tag, 
                'text': p.text, 
                'image': f'media/{p.image.name}',
                'created_date': p.formatted_date,
                'views': p.views.count(),
                'likes': p.likes.count(),
                'comments': p.comments.count() 
            } for p in posts]
    posts = [posts[i] if i < len(posts) else {} for i in range(10) ]
    return render(request, 'index.html', context={'latest': posts[0], 'other': posts[1:]})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.first()
            post.created_date = timezone.now()
            try:
                post.image = request.FILES['image']
            except Exception:
                pass
            post.save()
            return redirect('index')
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})