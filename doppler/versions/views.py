from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from models import Versions
from serializers import VersionsSerializer

class VersionsViewSet(viewsets.ModelViewSet):
    queryset = Versions.objects.all()
    serializer_class = VersionsSerializer