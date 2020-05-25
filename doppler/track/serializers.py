from rest_framework import serializers

from models import Track

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'track_id',
            'track_name',
            'track_key',
            'track_lyrics',
            'track_authors',
            'last_modify_date',
            'version',
            'private'

        )

    