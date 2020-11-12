from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):

    context={
        'posts':Post.objects.all()
    }
    return render(request, 'posts/index.html', context)