from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.musician_form,name="MusicianForm"),
    path('edit/<int:id>',views.edit_musician,name="EditMusician"),
]