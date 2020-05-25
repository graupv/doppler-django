from django.db import models

class Versions(models.Model):
    version = models.PositiveIntegerField()
    key = models.CharField(verbose_name="track_key", null=True, editable=True)
    name = models.CharField(verbose_name="track_name", blank=False)
    lyrics = models.CharField(verbose_name='track_lyrics', null=True)
    authors = models.CharField(verbose_name='track_authors', null=False)
    modify_date = models.DateTimeField()
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