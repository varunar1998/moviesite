from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def demo(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'result':obj})


