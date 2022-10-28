import requests
from base.models import Album, Photos
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://jsonplaceholder.typicode.com/photos'


class Command(BaseCommand):
    def import_photos(self, data):
        title = data.get('title')
        albumId = data.get('albumId')
        album = Album.objects.get(id=albumId)
        url = data.get('url')
        try:
            photo, created = Photos.objects.get_or_create(
                title=title,
                album=album,
                image_url=url
            )
            if created:
                photo.save()
                display_format = '\nPhoto, {}, has been saved'
                print(display_format.format(photo))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this photo: {}\n{}".format(title, str(ex))
            print(msg)

    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )
        response.raise_for_status()
        data = response.json()
        for data_object in data:
            self.import_photos(data_object)
