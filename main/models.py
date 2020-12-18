from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    
    #fields for movie table
    
    name = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=2000)
    description = models.TextField(max_length=5000)
    release_Date = models.DateField()
    average_Rating = models.FloatField()
    image = models.URLField(default=None, null=True)

    def __str__(self): 
        return self.name  

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
