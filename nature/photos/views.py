from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def single_image(request,post_id):
    return render(request,'single_image.html')
