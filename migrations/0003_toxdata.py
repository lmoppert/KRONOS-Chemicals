# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0002_auto_20150121_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toxdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tox', models.BooleanField(default=False)),
                ('oekotox', models.BooleanField(default=False)),
                ('chemical', models.ForeignKey(to='chemicals.Chemical')),
                ('supplier', models.ForeignKey(to='chemicals.Contact')),
            ],
            options={
                'verbose_name': 'Tox Oekotox',
                'verbose_name_plural': 'Tox Oekotox',
            },
            bases=(models.Model,),
        ),
    ]
