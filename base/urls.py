from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('photos', views.PhotosView, 'photolist')
router.register('albums', views.AlbumView, 'albumlist')
router.register('add_photo', views.PhotosCreateView, 'addphoto')


urlpatterns = [
    path('', include(router.urls)),
    path('albums/<int:id>', views.AlbumUpdateView.as_view()),
    path('photos/<int:pk>/', views.PhotosDetailView.as_view(), name='photo_details'),
]
