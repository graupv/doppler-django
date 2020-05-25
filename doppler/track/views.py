from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from models import Track
from serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer