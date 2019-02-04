from django.db import models
import datetime
from django.contrib.postgres.fields import JSONField
from taggit.managers import TaggableManager

class Feat(models.Model):

    created = models.DateField(default=datetime.datetime.now())
    updated = models.DateField(default=datetime.datetime.now())

    name = models.CharField(max_length=80)
    description = models.TextField()
    success = models.TextField(null=True)
    crit_success = models.TextField(null=True)
    fail = models.TextField(null=True)
    crit_failure = models.TextField(null=True)

    special = models.TextField(null=True)

    level = models.SmallIntegerField()
    trigger = models.TextField(null=True)

    actions = models.SmallIntegerField(null=True)
    traits = JSONField(null=True)
    tags = TaggableManager()
