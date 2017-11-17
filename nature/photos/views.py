from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def single_image(request):
    return render(request,'single_image.html')
