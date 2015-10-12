# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0010_auto_20151001_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachescareer',
            name='year',
        ),
    ]
