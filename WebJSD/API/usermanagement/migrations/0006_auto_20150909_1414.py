# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0005_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.TimeField(),
        ),
    ]
