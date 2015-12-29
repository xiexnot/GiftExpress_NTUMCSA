# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identify', models.CharField(max_length=5)),
                ('exchange_flag', models.BooleanField(default=False)),
                ('sex', models.CharField(default=b'Female', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identify', models.CharField(max_length=5)),
                ('exchange_flag', models.BooleanField(default=False)),
                ('sex', models.CharField(default=b'Male', max_length=10)),
            ],
        ),
    ]
