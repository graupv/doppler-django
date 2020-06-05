from rest_framework import serializers

from models import Chordbox

class ChordboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chordbox
        fields = (
            'chords',
            'username'

        )