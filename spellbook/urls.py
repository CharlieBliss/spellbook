"""spellbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.urls import path
from django.contrib.auth.models import User
from django.conf.urls import url, include
from .spells.views import SpellViewSet, SpellListView
from .characters.views import CharacterViewSet
from .feats.views import FeatListView, FeatViewSet

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='characters')
router.register(r'users', UserViewSet)
router.register(r'spells', SpellViewSet)
router.register(r'feats', FeatViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('spell', SpellListView.as_view(), name='spells'),
    path('feat', FeatListView.as_view(), name='feats'),
    url(r'^api-auth/', include('rest_framework.urls'))
]
