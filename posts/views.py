from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'message':'This is my first message',
        'message2':'Second message',
    }
    return render(request, 'posts/index.html', context)