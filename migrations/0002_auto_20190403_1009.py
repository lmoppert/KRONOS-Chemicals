# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='cas',
            field=models.CharField(max_length=200, null=True, verbose_name='CAS', blank=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='einecs',
            field=models.CharField(max_length=200, null=True, verbose_name='EINECS', blank=True),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='registration_number',
            field=models.CharField(max_length=200, null=True, verbose_name='Registration Number', blank=True),
        ),
    ]
