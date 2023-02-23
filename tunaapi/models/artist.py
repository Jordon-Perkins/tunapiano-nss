from django.db import models
from .song import Song


class Artist(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    bio = models.CharField(max_length=200)

# the single definitive source of information about your DB showing essential fields and behaviors of your data

    @property
    def number_of_songs(self):
        return Song.objects.filter(artist_id = self.pk).count()

    
    