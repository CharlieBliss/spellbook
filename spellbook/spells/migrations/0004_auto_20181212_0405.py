# Generated by Django 2.1.4 on 2018-12-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0003_auto_20181212_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='updated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
