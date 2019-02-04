from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Feat
from .serializers import FeatSerializer

class FeatViewSet(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    serializer_class = FeatSerializer


class FeatListView(generics.ListAPIView):
    queryset = Feat.objects.all()
    serializer_class = FeatSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('level',)