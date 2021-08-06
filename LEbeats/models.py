from django.conf import settings
from django.db import models
from django.db.models.fields.related import ForeignKey
# from django.utils import timezone


class Artist(models.Model):
    artist = models.CharField(max_length=40)

    def __str__(self):
        return self.artist
    
    class Meta:
        ordering = ["artist"]

class Album(models.Model):
#    settings.AUTH_USER_MODEL
    artist = models.ForeignKey(to=Artist, related_name='albums', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


        