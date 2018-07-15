# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . models import Location, Category, Image
# Create your views here.

def index(request):
    images = Image.objects.all()
    imagelocation = Location.objects.all()
    imagecategory = Category.objects.all()

    args = {'images': images, 'imagelocation':imagelocation, 'imagecategory':imagecategory }
    
    return render(request, 'index.html', args)
    

# def category(request):
#     imagecategory = Category.objects.all()
#     # args = {'imagecategory': imagecategory}

    return render (request, 'categories.html', args)

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get('image')
        searched_images = Image.search_by_category(image_category)
        message = f"{category}"
        args = {"images": searched_images}
        return render(request, "search.html", args)
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message":message})


# keith mzaza
# def search_results(request):
#    if 'image' in request.GET and request.GET["image"]:
#        category = request.GET.get('image')
#        searched_images = Image.search_image(category)
#        message = f"{category}"
#        return render(request, 'search.html', {"message": message, "images": searched_images})
#    else:
#        message = "You haven't searched for any term"
#        return render(request, 'search.html', {'message': message})
 
# def display_by_category(request):
#     images = Image.image_category()
#     args = {'images': images}
#     return render(request, 'categories.html', args)

# def display_by_location(request):
#     images = Image.image_location()
#     args = {'images':images}
#     return render(request, 'areas.html', args)