# Generated by Django 2.1.4 on 2018-12-12 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0015_auto_20181212_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 12, 12, 4, 23, 12, 259791)),
        ),
        migrations.AlterField(
            model_name='spell',
            name='updated',
            field=models.DateField(default=datetime.datetime(2018, 12, 12, 4, 23, 12, 259843)),
        ),
    ]
