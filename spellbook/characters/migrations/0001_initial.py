# Generated by Django 2.1.4 on 2018-12-17 20:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spells', '0017_auto_20181217_2004'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feats', '0004_auto_20181217_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(default=datetime.datetime(2018, 12, 17, 20, 4, 7, 833174))),
                ('updated', models.DateField(default=datetime.datetime(2018, 12, 17, 20, 4, 7, 833266))),
                ('name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=300)),
                ('thumbnail', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('character_class', models.CharField(max_length=80)),
                ('feats', models.ManyToManyField(to='feats.Feat')),
                ('spells', models.ManyToManyField(to='spells.Spell')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
