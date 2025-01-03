# Generated by Django 5.1.4 on 2024-12-23 23:44

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=datetime.datetime(2024, 12, 23, 23, 44, 21, 982302, tzinfo=datetime.timezone.utc), max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
