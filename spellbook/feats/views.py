from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Feat
from .serializers import FeatSerializer

class FeatViewSet(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    serializer_class = FeatSerializer


class FeatListView(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    serializer_class = FeatSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('name', 'level')

    def get_queryset(self):
        params = self.request.query_params
        queryset = Feat.objects.filter(
            level__gt=params.get('level_gt', 0)).filter(
                level__lt=params.get('level_lt', 10))
        if 'search' in params:
            queryset = queryset.filter(name__icontains=params.get('search', ''))
        if 'traits' in params:
            queryset = queryset.filter(traits__icontains=params.get('traits', ''))

        return queryset