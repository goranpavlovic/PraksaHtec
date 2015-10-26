# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0010_auto_20150910_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='producer',
        ),
        migrations.AddField(
            model_name='album',
            name='producer',
            field=models.ForeignKey(to='usermanagement.ProductionHouse', null=True),
        ),
    ]
