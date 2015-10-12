# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0011_remove_coachescareer_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersPlayOff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.CharField(max_length=15, db_index=True)),
                ('first_name', models.CharField(max_length=50, null=True, editable=False)),
                ('last_name', models.CharField(max_length=50, null=True, editable=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('team', models.CharField(max_length=15)),
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
        migrations.CreateModel(
            name='PlayersRegularSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_id', models.CharField(max_length=15, db_index=True)),
                ('first_name', models.CharField(max_length=50, null=True, editable=False)),
                ('last_name', models.CharField(max_length=50, null=True, editable=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('team', models.CharField(max_length=15)),
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
