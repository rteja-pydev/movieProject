from django.db import models

# Create your models here.
class Movie(models.Model):
    ryear=models.IntegerField()
    moviename=models.CharField(max_length=60)
    hero=models.CharField(max_length=60)
    heroine=models.CharField(max_length=60)
    rating=models.FloatField()
