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

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Post.search_by_tags(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message = "No images searched"
        return render(request,'search.html',{"message":message})
