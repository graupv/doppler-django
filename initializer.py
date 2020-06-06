#   desde venv

from django.contrib.auth.models import User 
from track.models import Track

user = User.objects.create(username='usuario', password='1234', email=em@il)
user.save()

track = Track(id=1, name='my song', username=user.username, lyrics='words', key='A', version=1)
track.save()