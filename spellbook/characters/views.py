from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user.id)
