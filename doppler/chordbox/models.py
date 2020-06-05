from django.db import models
# from django.contrib.auth.models import User

class Chordbox(models.Model):
    chords = models.CharField(max_length=32)
    username = models.CharField(max_length=100, null=True)