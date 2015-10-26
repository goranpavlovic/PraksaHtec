# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0003_musician_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
