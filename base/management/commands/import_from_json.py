import os
import json
from base.models import Photos, Album
from django.core.management.base import BaseCommand
from managing_photos.settings import BASE_DIR


class Command(BaseCommand):
    def photo_from_json(self):
        data_folder = os.path.join(BASE_DIR, 'base', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    title = data_object.get('title')
                    albumId = data_object.get('albumId')
                    album = Album.objects.get(id=albumId)
                    url = data_object.get('url')

                    try:
                        photo, created = Photos.objects.get_or_create(
                            title=title,
                            album=album,
                            image_url=url
                        )
                        if created:
                            photo.save()
                            display_format = "\nPhoto, {}, has been saved."
                            print(display_format.format(photo))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this photo: {}\n{}".format(title, str(ex))
                        print(msg)

    def handle(self, *args, **options):
        self.photo_from_json()
