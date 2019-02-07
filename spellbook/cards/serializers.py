from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'name',
            'id',
            'content',
            'x_position',
            'y_position',
            'board',
            'image',
        )