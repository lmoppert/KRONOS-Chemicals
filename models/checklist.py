"""Models that are related to the checklist for a chemical."""

from django.db import models
from django.conf import settings
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _


class CheckUsage(models.Model):
    """Checklists are meant for a specific use case."""

    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Check List Usage")


class CheckList(models.Model):
    """Core-Model for the Checklists."""

    STATES = (('o', _('open')), ('a', _('active')), ('c', _('closed')),)

    department = models.ForeignKey('Department')
    chemical = models.ForeignKey('Chemical')
    usage = models.ForeignKey(CheckUsage)
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES)
    status = models.CharField(max_length=1, choices=STATES)
    started_on = models.DateField()
    started_by = models.ForeignKey('Person', related_name='initiator')
    closed_on = models.DateField()
    closed_by = models.ForeignKey('Person', related_name='closer')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Check List")


class CheckSection(models.Model):
    """Checklists are split into sections."""

    checklist = models.ForeignKey(CheckList)
    description = models.TextField()
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Check List Section")


class PPE(models.Model):
    """Personal Protective Equipment, english translation for PSA."""

    description = models.TextField()
    image = FilerImageField(null=False, blank=False)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Personal Protective Equipment (PPE)")


class HPhraseCheck(models.Model):
    """Class holding the check information of a h-phrase."""

    checklist = models.ForeignKey(CheckList)
    hphrase = models.ForeignKey('HPhrase')
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("H Phrase")


class PPhraseCheck(models.Model):
    """Class holding the check information of a p-phrase."""

    checklist = models.ForeignKey(CheckList)
    pphrase = models.ForeignKey('PPhrase')
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("P Phrase")


class WGKCheck(models.Model):
    """Class holding the check information of a WGK."""

    checklist = models.ForeignKey(CheckList)
    pphrase = models.ForeignKey('WGK')
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("WGK")


class PictogramCheck(models.Model):
    """Class holding the check information of a pictogram."""

    checklist = models.ForeignKey(CheckList)
    pphrase = models.ForeignKey('Pictogram')
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Pictogram Check")


class StorageClassCheck(models.Model):
    """Class holding the check information of a storage class."""

    checklist = models.ForeignKey(CheckList)
    pphrase = models.ForeignKey('PPhrase')
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Storage Class Check")


class PPECheck(models.Model):
    """Class holding the check information of a PPE."""

    checklist = models.ForeignKey(CheckList)
    ppe = models.ForeignKey(PPE)
    info_department = models.BooleanField(default=False)
    info_person = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    done_date = models.DateField()
    done_by = models.ForeignKey('Person')

    class Meta:
        app_label = "chemicals"
        verbose_name = _("PPE Check")
