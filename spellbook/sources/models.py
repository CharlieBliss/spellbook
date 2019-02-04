from django.db import models

class Source(models.Model):

    created = models.DateField()
    updated = models.DateField()

    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    pubisher = models.CharField(max_length=80)
    official = (
        ('y', "Yes"),
        ('n', "No"),
        ('b', "Beta"),
        ('t', "Third-party"),
    )
