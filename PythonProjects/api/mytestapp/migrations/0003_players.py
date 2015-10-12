# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mytestapp', '0002_delete_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, editable=False)),
                ('last_name', models.CharField(max_length=50, null=True, editable=False)),
                ('position', models.CharField(default=b'G', max_length=2, null=True, choices=[(b'C', b'Center'), (b'F', b'Forward'), (b'PF', b'Power Forward'), (b'G', b'Guard'), (b'PG', b'Power Guard')])),
                ('first_season', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('last_season', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2015)])),
                ('height_feet', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(8.0)])),
                ('height_inches', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(59.0), django.core.validators.MaxValueValidator(94.0)])),
                ('weight', models.FloatField(null=True)),
                ('college', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
