from django.shortcuts import render
from Album.models import Album
from Musician.models import Musician
def home(request):
    album=Album.objects.all()
    return render(request,'home.html',{'album':album})