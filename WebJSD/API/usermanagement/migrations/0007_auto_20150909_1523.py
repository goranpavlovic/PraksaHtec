# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0006_auto_20150909_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.TimeField(null=True),
        ),
    ]
