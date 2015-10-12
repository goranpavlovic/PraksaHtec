# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0005_auto_20150930_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayersAllStar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('all_star_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1947), django.core.validators.MaxValueValidator(2015)])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('conference', models.CharField(max_length=50)),
                ('minutes', models.IntegerField(null=True)),
                ('points', models.IntegerField(null=True)),
                ('off_rebounds', models.IntegerField(null=True)),
                ('def_rebounds', models.IntegerField(null=True)),
                ('rebounds', models.IntegerField(null=True)),
                ('assists', models.IntegerField(null=True)),
                ('steals', models.IntegerField(null=True)),
                ('blocks', models.IntegerField(null=True)),
                ('turnovers', models.IntegerField(null=True)),
                ('all_player_id', models.ForeignKey(to='mytestapp.Players')),
            ],
        ),
    ]
