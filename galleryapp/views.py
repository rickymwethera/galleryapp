from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category

# Create your views here.

def welcome(request):
    images = Image.get_images()
    locations = Location.get_locations()
    return render(request, 'index.html',{"images":images, 'locations': locations})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for an image"
        return render(request, 'search.html',{"message":message})

def image_location(request, location):
    images = Image.filter_by_location(location)
    message = f"{location}"
    return render(request, 'location.html', {"message":message,'images': images})
