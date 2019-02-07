from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from .models import Board
from ..cards.models import Card
from .serializers import BoardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(user=user.id)
