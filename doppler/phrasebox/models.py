from django.db import models

# from django.contrib.auth.models import User

class Phrasebox(models.Model):
    phrases = models.CharField(max_length=5000)
    words = models.CharField(max_length=5000)
    username = models.CharField(max_length=100, null=True)