from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Track(models.Model):
    track_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(verbose_name="track_name", blank=False, max_length=200)
    key = models.CharField(verbose_name="track_key", null=True, editable=True, max_length=2)
    lyrics = models.CharField(verbose_name='track_lyrics', null=True, max_length=6000)
    modify_date = models.DateTimeField(auto_now=True)
    version = models.PositiveIntegerField()
    username = models.CharField(max_length=100, null=True)
    # owner = models.CharField(verbose_name='track_owner', null=False, max_length=32)
    private = models.BooleanField(default=True)

    # class Meta:
    #     constraints = [
    #         # models.UniqueConstraint(fields=['track_id', 'version'], name='unique_track_id_version')
    #     ]   

    def __str__(self):
        return f'Track Name: {self.name} Track Author: {self.username} Track Version: {self.version} Private: {"Yes" if self.private else "no"}'