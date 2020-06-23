from django.contrib.postgres.fields import ArrayField
from django.db import models

# from django.contrib.auth.models import User

class Phrasebox(models.Model):
    # phrases = models.CharField(max_length=5000)
    phrases = ArrayField(
        models.CharField(max_length=200, blank=True),

    )
    # words = models.CharField(max_length=5000)
    # words = ArrayField(
    #     models.CharField(max_length=200, blank=True),
        
    # )
    username = models.CharField(max_length=100, primary_key=True)

    