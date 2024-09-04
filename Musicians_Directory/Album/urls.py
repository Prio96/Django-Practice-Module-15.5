from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.album_form,name="AlbumForm")
]