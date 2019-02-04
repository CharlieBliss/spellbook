from django.db import models
import datetime
from django.contrib.postgres.fields import JSONField
from ..feats.models import Feat
from ..spells.models import Spell
from django.contrib.auth.models import User


class Character(models.Model):

    created = models.DateField(default=datetime.datetime.now())
    updated = models.DateField(default=datetime.datetime.now())

    name = models.CharField(max_length=80)
    image = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=300)
    description = models.TextField()
    character_class = models.CharField(max_length=80)
    feats = models.ManyToManyField(Feat)
    spells = models.ManyToManyField(Spell)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


from django.db import models

# Create your models here.
