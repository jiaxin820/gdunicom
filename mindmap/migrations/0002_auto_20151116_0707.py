# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mindmap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapsearch',
            name='map_id',
        ),
        migrations.RemoveField(
            model_name='mapdetail',
            name='last_update',
        ),
        migrations.AddField(
            model_name='mapdetail',
            name='search_text',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 7, 7, 27, 226790, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mapdetail',
            name='version',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='MapSearch',
        ),
    ]
