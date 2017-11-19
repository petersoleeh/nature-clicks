from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
def index(request):
    posts = Post.all_posts()
    return render(request,'index.html',{"posts":posts})

def single_image(request,post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("The Post does not exist")

    return render(request,'single_image.html',{"post":post})


def contacts(request):
    return render(request,'contacts.html')
