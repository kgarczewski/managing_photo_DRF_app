from django.db import models
from colorthief import ColorThief
import matplotlib.pyplot as plt
import urllib.request
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

headers = {'User-Agent': 'Mozilla/5.0'}


class Album(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Photos(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums', null=True,
                              blank=True, default=None)
    title = models.CharField(max_length=200)
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images/', blank=True, width_field='image_width',
                                   height_field='image_height')
    image_url = models.URLField(max_length=500, blank=True, null=True)
    dominant_color = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            req = urllib.request.Request(self.image_url, headers=headers)
            img_temp.write(urlopen(req, timeout=10).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.title}", File(img_temp))
        self.image_file.open()
        ct = ColorThief(self.image_file)
        dominant_c = ct.get_color(quality=1)
        plt.imshow([[dominant_c]])
        dominant = ('#%02x%02x%02x' % dominant_c)
        self.dominant_color = dominant
        self.save_base()
