from rest_framework import serializers
from .models import Character
from ..feats.serializers import FeatSerializer

class CharacterSerializer(serializers.HyperlinkedModelSerializer):

    # spells = serializers.HyperlinkedIdentityField(view_name="spellbook:spells")

    class Meta:
        model = Character
        fields = (
            'name',
            'description',
            'image',
            'feats',
            'spells',
            'thumbnail',
            'character_class'
        )