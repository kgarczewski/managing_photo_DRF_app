from rest_framework.pagination import PageNumberPagination
from base.models import Album, Photos
from base.serializers import PhotosSerializer, PhotosUpdateSerializer, AlbumSerializer, AlbumUpdateSerializer, \
    PhotoCreateSerializer
from rest_framework import generics
from rest_framework.viewsets import ViewSetMixin
# Create your views here.


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 5000


IMPORT_URL = 'https://jsonplaceholder.typicode.com/photos'


class AlbumView(ViewSetMixin, generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = LargeResultsSetPagination


class AlbumUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer
    lookup_field = "id"


class PhotosView(ViewSetMixin, generics.ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    pagination_class = LargeResultsSetPagination


class PhotosCreateView(ViewSetMixin, generics.CreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoCreateSerializer
    pagination_class = LargeResultsSetPagination


class PhotosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotosUpdateSerializer
