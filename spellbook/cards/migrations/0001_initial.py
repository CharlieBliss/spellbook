# Generated by Django 2.1.5 on 2019-02-06 03:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0002_auto_20190206_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(default=datetime.datetime(2019, 2, 6, 3, 32, 7, 957655))),
                ('updated', models.DateField(default=datetime.datetime(2019, 2, 6, 3, 32, 7, 957732))),
                ('name', models.CharField(max_length=80)),
                ('content', django_bleach.models.BleachField()),
                ('x_position', models.SmallIntegerField()),
                ('y_posiiton', models.SmallIntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='boards.Board')),
            ],
        ),
    ]
