# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0004_playerscareer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerscareer',
            name='player_id',
            field=models.CharField(max_length=15, db_index=True),
        ),
    ]
