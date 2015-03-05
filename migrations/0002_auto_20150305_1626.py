# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chemicals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departments', models.ManyToManyField(to='chemicals.Department', verbose_name='Managed Department')),
                ('user', models.OneToOneField(verbose_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='departmentadmin',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='departmentadmin',
            name='user',
        ),
        migrations.DeleteModel(
            name='DepartmentAdmin',
        ),
    ]
