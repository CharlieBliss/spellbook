from rest_framework import serializers
from .models import Spell

class SpellSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Spell
        fields = (
            'name',
            'description',
            'success',
            'crit_success',
            'fail',
            'crit_failure',
            'level',
            'area',
            'range',
            'duration',
            'target',
            'trigger',
            'type',
            'verbal',
            'somatic',
            'material',
            'table',
        )