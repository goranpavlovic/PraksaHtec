# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0007_auto_20150909_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
