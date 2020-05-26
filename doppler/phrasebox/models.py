from django.db import models

from django.contrib.auth.models import User

class Phrasebox(models.Model):
    phrases = models.CharField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)