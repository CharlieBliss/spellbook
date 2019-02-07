from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
import django_filters

from .models import Spell
from .serializers import SpellSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellListView(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('name', 'level')

    def get_queryset(self):
        params = self.request.query_params
        queryset = Spell.objects.filter(
            level__gt=params.get('level_gt', 0)).filter(
                level__lt=params.get('level_lt', 10))
        if 'search' in params:
            queryset = queryset.filter(name__icontains=params.get('search', ''))
        if 'type' in params:
            queryset = queryset.filter(type__icontains=params.get('type', ''))
        if 'traits' in params:
            queryset = queryset.filter(traits__icontains=params.get('traits', ''))

        return queryset