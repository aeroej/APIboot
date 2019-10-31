from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk','title','body','author_name')

class AlbumSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk','author','image','desc')

class FileSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    mygile= serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk','author','mygile','desc')
