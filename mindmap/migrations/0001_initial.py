# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_text', models.TextField()),
                ('last_update', models.DateTimeField(verbose_name=b'last update date')),
            ],
        ),
        migrations.CreateModel(
            name='MapSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('search_text', models.TextField()),
                ('map_id', models.ForeignKey(to='mindmap.MapDetail')),
            ],
        ),
    ]
