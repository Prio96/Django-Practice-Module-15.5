from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.album_form,name="AlbumForm"),
    path('edit/<int:id>',views.edit_album,name="EditAlbum"),
    path('delete/<int:id>',views.delete_album,name="DeleteAlbum"),
]