from django.db import models


# Create your models here.
class MyTestModel(models.Model):
    test_field = models.TextField()


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=30, null=True)


class ProductionHouse(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    founded = models.DateField()
    budget = models.IntegerField()


class Album(models.Model):
    artist = models.ForeignKey(Musician)
    producer = models.ForeignKey(ProductionHouse, null=True)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=50)
    duration = models.TimeField(null=True)




