# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0006_playersallstar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playersallstar',
            old_name='all_player_id',
            new_name='all_player',
        ),
    ]
