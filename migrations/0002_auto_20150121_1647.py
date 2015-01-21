# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checklist',
            options={'verbose_name': 'Check List', 'verbose_name_plural': 'Check Lists'},
        ),
        migrations.AlterModelOptions(
            name='checksection',
            options={'verbose_name': 'Check List Section', 'verbose_name_plural': 'Check List Sections'},
        ),
        migrations.AlterModelOptions(
            name='checkusage',
            options={'verbose_name': 'Check List Usage', 'verbose_name_plural': 'Check List Usages'},
        ),
        migrations.AlterModelOptions(
            name='chemical',
            options={'verbose_name': 'Chemical', 'verbose_name_plural': 'Chemicals'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='extendedsafetydatasheet',
            options={'verbose_name': 'Extended Safety Data Sheet', 'verbose_name_plural': 'Extended Safety Data Sheets'},
        ),
        migrations.AlterModelOptions(
            name='hphrase',
            options={'verbose_name': 'H Phrase', 'verbose_name_plural': 'H Phrases'},
        ),
        migrations.AlterModelOptions(
            name='hphrasecheck',
            options={'verbose_name': 'H Phrase', 'verbose_name_plural': 'H Phrases'},
        ),
        migrations.AlterModelOptions(
            name='hphraserelation',
            options={'verbose_name': 'H Phrase Relation', 'verbose_name_plural': 'H Phrase Relations'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='pictogram',
            options={'verbose_name': 'Pictogram', 'verbose_name_plural': 'Pictograms'},
        ),
        migrations.AlterModelOptions(
            name='pictogramcheck',
            options={'verbose_name': 'Pictogram Check', 'verbose_name_plural': 'Pictogram Checks'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'Plant', 'verbose_name_plural': 'Plants'},
        ),
        migrations.AlterModelOptions(
            name='ppe',
            options={'verbose_name': 'Personal Protective Equipment (PPE)', 'verbose_name_plural': 'Personal Protective Equipments (PPE)'},
        ),
        migrations.AlterModelOptions(
            name='ppecheck',
            options={'verbose_name': 'PPE Check', 'verbose_name_plural': 'PPE Checks'},
        ),
        migrations.AlterModelOptions(
            name='pphrase',
            options={'verbose_name': 'P Phrase', 'verbose_name_plural': 'P Phrases'},
        ),
        migrations.AlterModelOptions(
            name='pphrasecheck',
            options={'verbose_name': 'P Phrase', 'verbose_name_plural': 'P Phrases'},
        ),
        migrations.AlterModelOptions(
            name='reachdocument',
            options={'verbose_name': 'Reach Document', 'verbose_name_plural': 'Reach Documents'},
        ),
        migrations.AlterModelOptions(
            name='reachinformation',
            options={'verbose_name': 'Reach Information', 'verbose_name_plural': 'Reach Information'},
        ),
        migrations.AlterModelOptions(
            name='risk',
            options={'verbose_name': 'Risk', 'verbose_name_plural': 'Risks'},
        ),
        migrations.AlterModelOptions(
            name='riskindication',
            options={'verbose_name': 'Risk Indication', 'verbose_name_plural': 'Risk Indications'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='rphrase',
            options={'verbose_name': 'R Phrase', 'verbose_name_plural': 'R Phrases'},
        ),
        migrations.AlterModelOptions(
            name='safetydatasheet',
            options={'verbose_name': 'Safety Data Sheet', 'verbose_name_plural': 'Safety Data Sheets'},
        ),
        migrations.AlterModelOptions(
            name='sevesocategory',
            options={'verbose_name': 'Seveso Category', 'verbose_name_plural': 'Seveso Categories'},
        ),
        migrations.AlterModelOptions(
            name='sevesodocument',
            options={'verbose_name': 'Seveso Document', 'verbose_name_plural': 'Seveso Documents'},
        ),
        migrations.AlterModelOptions(
            name='sevesoinformation',
            options={'verbose_name': 'Seveso Information', 'verbose_name_plural': 'Seveso Information'},
        ),
        migrations.AlterModelOptions(
            name='signal',
            options={'verbose_name': 'Singal', 'verbose_name_plural': 'Singals'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Stock', 'verbose_name_plural': 'Stocks'},
        ),
        migrations.AlterModelOptions(
            name='storageclass',
            options={'verbose_name': 'Storage Class', 'verbose_name_plural': 'Storage Classes'},
        ),
        migrations.AlterModelOptions(
            name='storageclasscheck',
            options={'verbose_name': 'Storage Class Check', 'verbose_name_plural': 'Storage Class Checks'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
        migrations.AlterModelOptions(
            name='synonym',
            options={'verbose_name': 'Chemical Synonym', 'verbose_name_plural': 'Chemical Synonyms'},
        ),
        migrations.AlterModelOptions(
            name='wgk',
            options={'verbose_name': 'WGK', 'verbose_name_plural': 'WGKs'},
        ),
        migrations.AlterModelOptions(
            name='wgkcheck',
            options={'verbose_name': 'WGK', 'verbose_name_plural': 'WGKs'},
        ),
    ]
