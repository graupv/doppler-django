from rest_framework import serializers

from track.models import Track

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'track_id',
            'track_name',
            'track_key',
            'track_lyrics',
            'username',
            'modify_date',
            'version',
            'private'

        )

    