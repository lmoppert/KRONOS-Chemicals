# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0004_remove_chemical_wgk'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemical',
            name='wgk',
            field=models.ManyToManyField(to='chemicals.WGK', blank=True),
            preserve_default=True,
        ),
    ]
