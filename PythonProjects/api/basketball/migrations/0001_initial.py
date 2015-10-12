# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, editable=False)),
                ('last_name', models.CharField(max_length=50, null=True, editable=False)),
                ('position', models.CharField(default=b'G', max_length=2, null=True, choices=[(b'C', b'Center'), (b'F', b'Forward'), (b'PF', b'Power Forward'), (b'G', b'Guard'), (b'PG', b'Power Guard')])),
                ('first_season', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('last_season', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('height_feet', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(8.0)])),
                ('height_inches', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(59.0), django.core.validators.MaxValueValidator(94.0)])),
                ('weight', models.FloatField(null=True)),
                ('college', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayersAllStar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
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
