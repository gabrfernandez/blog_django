from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def detail_view(request, id):
    #post = Post.objects.get(id=id)
    post= get_object_or_404(Post, id=id)
    context={
        'post':post
    }
    return render(request, 'posts/detail.html', context)

def create_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        return redirect(post.get_absolute_url())
    context = {
        'form' : form
    }
    return render(request, 'posts/create.html', context)