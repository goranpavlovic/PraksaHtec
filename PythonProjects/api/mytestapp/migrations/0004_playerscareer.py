# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0003_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersCareer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=50, null=True, editable=False)),
                ('last_name', models.CharField(max_length=50, null=True, editable=False)),
                ('games_played', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('points', models.IntegerField()),
                ('off_rebounds', models.IntegerField()),
                ('def_rebounds', models.IntegerField()),
                ('rebounds', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('blocks', models.IntegerField()),
                ('turnovers', models.IntegerField()),
            ],
        ),
    ]
