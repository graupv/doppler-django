from django.db import models

class Track(models.Model):
    track_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(verbose_name="track_name", blank=False)
    key = models.CharField(verbose_name="track_key", null=True, editable=True)
    lyrics = models.CharField(verbose_name='track_lyrics', null=True)
    authors = models.CharField(verbose_name='track_authors', null=False)
    modify_date = models.DateTimeField()
    version = models.PositiveIntegerField()
    private = models.BooleanField(default=True)

    # class Meta:
    #     constraints = [
    #         # models.UniqueConstraint(fields=['track_id', 'version'], name='unique_track_id_version')
    #     ]   

    def __str__(self):
        return f'Track Name: {self.name}/nTrack Author: {self.authors}/nTrack Version: {self.version}/nPrivate: {"Yes/n" if self.private else "no/n"}'