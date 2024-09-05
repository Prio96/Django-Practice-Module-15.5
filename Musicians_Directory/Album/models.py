from django.db import models
from Musician.models import Musician
# Create your models here.
class Album(models.Model):
    Album_name=models.CharField(max_length=200)
    Artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    Release_Date=models.DateField(auto_now_add=True)
    ratings=[
        (1,'1'),    
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    Rating=models.IntegerField(choices=ratings)
    
    def __str__(self):
        return f"{self.Album_name}"
    
