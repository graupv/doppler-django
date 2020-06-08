from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Versions(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.PositiveIntegerField()
    key = models.CharField(verbose_name="track_key", null=True, editable=True, max_length=2)
    name = models.CharField(verbose_name="track_name", blank=False, max_length=200)
    lyrics = models.CharField(verbose_name='track_lyrics', null=True, max_length=6000)
    # owner = models.OneToOneField(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    track_id = models.ForeignKey(
        'track.Track',
        on_delete=models.SET_NULL, 
        null=True, 
        max_length=32
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['track_id', 'version'], name='unique_track_id_version')
        ]

    def __str__(self):
        return f'Track Name: {self.name}/nVersion: {self.version}/n'