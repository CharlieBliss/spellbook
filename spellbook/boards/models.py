from django.db import models
import datetime
from django.contrib.auth.models import User


class Board(models.Model):

    created = models.DateField(default=datetime.datetime.now())
    updated = models.DateField(default=datetime.datetime.now())

    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
