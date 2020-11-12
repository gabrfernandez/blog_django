from django.shortcuts import render, get_object_or_404
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