# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0008_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoachesCareer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.CharField(max_length=10, null=True)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1947), django.core.validators.MaxValueValidator(2015)])),
                ('league', models.CharField(max_length=10, null=True)),
                ('o_fgm', models.IntegerField(null=True)),
                ('o_fga', models.IntegerField(null=True)),
                ('o_ftm', models.IntegerField(null=True)),
                ('o_fta', models.IntegerField(null=True)),
                ('o_oreb', models.IntegerField(null=True)),
                ('o_dreb', models.IntegerField(null=True)),
                ('o_reb', models.IntegerField(null=True)),
                ('o_asts', models.IntegerField(null=True)),
                ('o_pf', models.IntegerField(null=True)),
                ('o_stl', models.IntegerField(null=True)),
                ('o_to', models.IntegerField(null=True)),
                ('o_blk', models.IntegerField(null=True)),
                ('o_3pm', models.IntegerField(null=True)),
                ('o_3pa', models.IntegerField(null=True)),
                ('o_pts', models.IntegerField(null=True)),
                ('d_fgm', models.IntegerField(null=True)),
                ('d_fga', models.IntegerField(null=True)),
                ('d_ftm', models.IntegerField(null=True)),
                ('d_fta', models.IntegerField(null=True)),
                ('d_oreb', models.IntegerField(null=True)),
                ('d_dreb', models.IntegerField(null=True)),
                ('d_reb', models.IntegerField(null=True)),
                ('d_asts', models.IntegerField(null=True)),
                ('d_pf', models.IntegerField(null=True)),
                ('d_stl', models.IntegerField(null=True)),
                ('d_to', models.IntegerField(null=True)),
                ('d_blk', models.IntegerField(null=True)),
                ('d_3pm', models.IntegerField(null=True)),
                ('d_3pa', models.IntegerField(null=True)),
                ('d_pts', models.IntegerField(null=True)),
                ('pace', models.IntegerField(null=True)),
                ('won', models.IntegerField(null=True)),
                ('lost', models.IntegerField(null=True)),
            ],
        ),
    ]
