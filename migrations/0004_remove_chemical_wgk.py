# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0003_toxdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chemical',
            name='wgk',
        ),
    ]
