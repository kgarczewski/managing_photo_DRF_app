import requests
from base.models import Album
from django.core.management.base import BaseCommand
IMPORT_URL = 'https://jsonplaceholder.typicode.com/albums'


class Command(BaseCommand):
    def import_album(self, data):
        title = data.get('title')
        try:
            album, created = Album.objects.get_or_create(
                title=title
            )
            if created:
                album.save()
                display_format = '\nAlbum, {}, has been saved'
                print(display_format.format(album))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this album: {}\n{}".format(title, str(ex))
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
            self.import_album(data_object)
