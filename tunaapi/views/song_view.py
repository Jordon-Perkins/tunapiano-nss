"""View module for handling requests about game"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre, Artist, Song


class SongView(ViewSet):
    """Tuna Song view"""

    def retrieve(self, request, pk):
        """Handle GET requests for song 
        Returns:
            Response -- JSON serialized song 
        """
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songs 
        Returns:
            Response -- JSON serialized list of songs 
        """
        if "genre" in request.query_params:
            song = Song.objects.filter(genre_id = int(request.query_params['genre']))
        elif "artist" in request.query_params:
            song = Song.objects.filter(artist_id = int(request.query_params['artist']))
        else:
            song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized song instance
        """
        artist = Artist.objects.get(pk=request.data["artist"]) # retrieve artist to make sure it exists
        genre = Genre.objects.get(pk=request.data["genre"]) # retrieve genre to make sure it exists

        song = Song.objects.create(
            title=request.data["title"],
            artist=artist,
            genre=genre,
            album_name=request.data["album_name"],
            length=request.data["length"]
        )
        serializer = SongSerializer(song)
        return Response(serializer.data)

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ( 'name', )
        
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ( 'description', )



class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song 
    """

    genre = GenreSerializer()
    artist = ArtistSerializer()
    
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'genre', 'album_name', 'length', )