from django.db import models
from .genre import Genre


class Song(models.Model):
    title = models.CharField(max_length=55)
    artist = models.ForeignKey("tunaapi.Artist", on_delete=models.CASCADE, related_name= 'songs')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    album_name = models.CharField(max_length=55)
    length = models.IntegerField()