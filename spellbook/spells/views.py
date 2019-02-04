from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Spell
from .serializers import SpellSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellListView(generics.ListAPIView):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('level', 'type')