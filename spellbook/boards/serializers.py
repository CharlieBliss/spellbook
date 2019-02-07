from rest_framework import serializers
from .models import Board
from ..cards.serializers import CardSerializer

class BoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = (
            'name',
            'id',
            'cards'
        )