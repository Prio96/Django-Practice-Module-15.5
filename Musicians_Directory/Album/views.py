from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.
def album_form(request):
    if request.method=='POST':
        data=AlbumForm(request.POST)
        if data.is_valid():
            data.save()
            print(data.cleaned_data)
    else:
        data=AlbumForm()
    return render(request,'album_form.html',{'data':data})


def edit_album(request,id):
    album=Album.objects.get(pk=id)
    data=AlbumForm(instance=album)
    if request.method=='POST':
        data=AlbumForm(request.POST,instance=album)
        if data.is_valid():
            print(data.cleaned_data)
            data.save()
            return redirect("HomePage")
    return render(request,'album_form.html',{'data':data})


def delete_album(request,id):
    album=Album.objects.get(pk=id)
    album.delete()
    return redirect("HomePage")
            
