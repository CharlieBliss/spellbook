from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from .models import Card
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.request)
        return Card.objects.all()
