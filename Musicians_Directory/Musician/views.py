from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.
def musician_form(request):
    if request.method=='POST':
        form=MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=MusicianForm()
    return render(request,'musician_form.html',{'form':form})

def edit_musician(request,id):
    musician=Musician.objects.get(pk=id)
    form=MusicianForm(instance=musician)
    if request.method=='POST':
        form=MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("HomePage")
    return render(request,'musician_form.html',{'form':form})
        