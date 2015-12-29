# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='female',
            name='name',
            field=models.CharField(default=b'noname', max_length=50),
        ),
        migrations.AddField(
            model_name='male',
            name='name',
            field=models.CharField(default=b'noname', max_length=50),
        ),
        migrations.AlterField(
            model_name='female',
            name='identify',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='male',
            name='identify',
            field=models.IntegerField(),
        ),
    ]
