# Generated by Django 2.1.4 on 2018-12-12 04:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='crit_fail',
            new_name='crit_failure',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='spell',
            name='area',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='duration',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='heightened',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='level',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='range',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='rarity',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='target',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='traits',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[]),
            preserve_default=False,
        ),
    ]