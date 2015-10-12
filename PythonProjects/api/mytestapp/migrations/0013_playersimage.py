# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0012_playersplayoff_playersregularseason'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.CharField(max_length=15)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
