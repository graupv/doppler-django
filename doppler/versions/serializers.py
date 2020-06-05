from rest_framework import serializers

from versions.models import Versions

class VersionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Versions
        fields = (
            'version',
            'track_id',
            'track_name',
            'track_key',
            'track_lyrics',
            'modify_date',
            
        )

    