from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


def home__view(request):
    select=request.GET.get('selected_class')
    context={''}
    if select=='owner':
        owner=Owner.objects.all()
        context={'owner':owner}
    elif select=='gallery':
        gallery=Gallery.objects.all()
        context={'gallery':gallery}
    elif select=='car':
        car=Car.objects.all()
        context={'car':car}
    else:
        all=Car.objects.all()
        context={'all':all}
    return render(request,'home.html',context)

def gallery_view(request):
    select=request.GET.get('selected_gallery')
    gallery=Gallery.objects.all()
    context={'gallery':gallery}
    if select:
        selected_gallery = Gallery.objects.get(gallery=select) 
        all = Car.objects.filter(gallery=selected_gallery)
        context.update({'all': all})
    return render(request,'galleries.html',context)
    