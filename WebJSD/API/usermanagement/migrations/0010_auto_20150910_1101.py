# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0009_auto_20150909_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=30)),
                ('founded', models.DateField()),
                ('budget', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='producer',
            field=models.ForeignKey(to='usermanagement.ProductionHouse', null=True),
        ),
    ]
