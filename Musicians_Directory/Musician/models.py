from django.db import models

# Create your models here.
class Musician(models.Model):
    First_Name=models.CharField(max_length=35)
    Last_Name=models.CharField(max_length=35)
    Email=models.EmailField(name="Email Address")
    Phone=models.CharField(max_length=15,name="Phone Number")
    Instrument=models.CharField(max_length=30,name="Instrument Type")
    
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    
    