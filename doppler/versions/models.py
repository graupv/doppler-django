from django.db import models

class Versions(models.Model):
    version = models.PositiveIntegerField()
    name = models.CharField(verbose_name="track_name", blank=False)
    key = models.CharField(verbose_name="track_key", null=True, editable=True)
    lyrics = models.CharField(verbose_name='track_lyrics', )
    authors = models.CharField(verbose_name='authors')
    last_modify = models.DateTimeField(auto_now=True)
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