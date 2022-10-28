from rest_framework import serializers
from .models import Photos, Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title']


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title']


class PhotosSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field='id', queryset=Album.objects.all())

    class Meta:
        model = Photos
        fields = ['id', 'title', 'album','image_width', 'image_height', 'dominant_color', 'image_file']
        read_only_fields = [
            "image_width",
            "image_height",
            "dominant_color",
        ]
        extra_kwargs = {"input_field": {"write_only": True}}


class PhotoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photos
        fields = ['id', 'title', 'album', 'image_url']
        extra_kwargs = {"input_field": {"write_only": True}}


class PhotosUpdateSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field='id', queryset=Album.objects.all())

    class Meta:
        model = Photos
        fields = ['album', 'title', 'image_url']
