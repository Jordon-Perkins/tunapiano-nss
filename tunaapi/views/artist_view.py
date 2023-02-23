"""View module for handling requests about game"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artist, Song


class ArtistView(ViewSet):
    """Tuna artist view"""
# handles the methods on requests that the client has of the database for a single resource

    def retrieve(self, request, pk):
        """Handle GET requests for single artist 
        Returns:
            Response -- JSON serialized artist 
        """
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all artists 
        Returns:
            Response -- JSON serialized list of artists 
        """
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized artist instance
        """

        artist = Artist.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"]
        )
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ( 'id', 'title', 'album_name', )



class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artist 
    # process of converting a data structure into a format that can be stored or transmitted and reconstructed later
    """

    songs = SongSerializer(many=True)
    
    class Meta:
        model = Artist
        fields = ('id', 'name', 'age', 'bio', 'number_of_songs', 'songs', )

