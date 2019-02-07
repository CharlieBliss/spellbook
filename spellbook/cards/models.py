from django.db import models
import datetime
from ..boards.models import Board
from django_bleach.models import BleachField

# Create your models here.
class Card(models.Model):

    created = models.DateField(default=datetime.datetime.now())
    updated = models.DateField(default=datetime.datetime.now())

    name = models.CharField(max_length=80)
    content = BleachField(null=True)
    image = models.CharField(max_length=200, null=True)

    board = models.ForeignKey(Board, related_name='cards', on_delete=models.CASCADE)
    x_position = models.SmallIntegerField()
    y_position = models.SmallIntegerField()
