from rest_framework import serializers
from .models import Feat

class FeatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feat
        fields = (
            'name',
            'description',
            'success',
            'crit_success',
            'fail',
            'crit_failure',
            'level',
            'trigger',
            'actions',
        )