from rest_framework import serializers

from versions.models import Versions

class VersionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Versions
        fields = (
            'track_id',
            'name',
            'key',
            'lyrics',
            'version',
            'modify_date',
            
        )

    