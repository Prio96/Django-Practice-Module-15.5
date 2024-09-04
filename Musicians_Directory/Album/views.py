from django.shortcuts import render
from .forms import AlbumForm
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
