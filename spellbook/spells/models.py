from django.db import models
import datetime
from django.contrib.postgres.fields import JSONField
from taggit.managers import TaggableManager

class Spell(models.Model):

    created = models.DateField(default=datetime.datetime.now())
    updated = models.DateField(default=datetime.datetime.now())

    name = models.CharField(max_length=80)
    description = models.TextField()
    success = models.TextField(null=True)
    crit_success = models.TextField(null=True)
    fail = models.TextField(null=True)
    crit_failure = models.TextField(null=True)

    level = models.SmallIntegerField()
    area = models.CharField(max_length=80, null=True)
    range = models.CharField(max_length=80, null=True)
    target = models.TextField(null=True)
    rarity = models.SmallIntegerField()
    duration = models.CharField(max_length=80, null=True)
    heightened = JSONField(null=True)
    casting_time = models.CharField(max_length=80, null=True)
    trigger = models.TextField(null=True)
    # source = models.ForeignKey('Source', on_delete=models.CASCADE)

    type = models.CharField(max_length=80)
    verbal = models.BooleanField(null=True)
    somatic = models.BooleanField(null=True)
    material = models.TextField(null=True)
    traits = JSONField(null=True)
    tags = TaggableManager()
    table = JSONField(null=True)
