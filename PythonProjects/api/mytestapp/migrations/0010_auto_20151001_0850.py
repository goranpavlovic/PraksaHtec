# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0009_coaches_coachescareer_draft_teamseason'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Draft',
        ),
        migrations.AddField(
            model_name='coaches',
            name='coach_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='playoff_loss',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='playoff_win',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='season_loss',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='season_win',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='team',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='coaches',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='coach_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='playoff_loss',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='playoff_win',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='season_loss',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='season_win',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coachescareer',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
