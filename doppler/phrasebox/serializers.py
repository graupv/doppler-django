from rest_framework import serializers

from models import phrasebox

class PhraseboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = phrasebox
        field = (
            'id',
            'username',
            'phrases',
        )