# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_auto_20150908_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
