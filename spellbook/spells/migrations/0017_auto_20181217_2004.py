# Generated by Django 2.1.4 on 2018-12-17 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0016_auto_20181212_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='created',
            field=models.DateField(default=datetime.datetime(2018, 12, 17, 20, 4, 7, 815166)),
        ),
        migrations.AlterField(
            model_name='spell',
            name='updated',
            field=models.DateField(default=datetime.datetime(2018, 12, 17, 20, 4, 7, 815283)),
        ),
    ]