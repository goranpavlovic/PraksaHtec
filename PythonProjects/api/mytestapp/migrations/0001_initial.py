# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyTestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_field', models.TextField()),
            ],
        ),
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
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.TimeField(null=True)),
                ('album', models.ForeignKey(to='mytestapp.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='mytestapp.Musician'),
        ),
        migrations.AddField(
            model_name='album',
            name='producer',
            field=models.ForeignKey(to='mytestapp.ProductionHouse', null=True),
        ),
    ]
