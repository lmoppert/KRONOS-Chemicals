"""Models that are related to a substance."""

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.utils.translation import ugettext_lazy as _


class HPhrase(models.Model):
    """Simple class for storing H phrases of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("H-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True)
    seveso_relevant = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("H Phrase")
        verbose_name_plural = _("H Phrases")


class PPhrase(models.Model):
    """Simple class for storing P phrases of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("P-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("P Phrase")
        verbose_name_plural = _("P Phrases")


class RPhrase(models.Model):
    """Simple class for storing R phrases of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("R-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("R-Phrase")
        verbose_name_plural = _("R-Phrases")


class SevesoCategory(models.Model):
    """Class for the Seveso category of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("Seveso Category"))
    description = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Seveso Category")
        verbose_name_plural = _("Seveso Categories")


class StorageClass(models.Model):
    """Class for the storage class of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("Storage Class"))
    description = models.CharField(max_length=400)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Storage Class")
        verbose_name_plural = _("Storage Classes")


class Synonym(models.Model):
    """Simple Class for storing synonyms of chemicals."""

    name = models.CharField(max_length=100, verbose_name=_("Synonym"))

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Chemical Synonym")
        verbose_name_plural = _("Chemical Synonyms")


class WGK(models.Model):
    """Simple class for storing the WGK of a chemical."""

    name = models.CharField(max_length=20, verbose_name=_("WGK"))
    description = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("WGK")
        verbose_name_plural = _("WGKs")


class RiskIndication(models.Model):
    """Simple class for the risk class of a chemical."""

    name = models.CharField(max_length=100, verbose_name=_("Risk"))

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Risk Indication")
        verbose_name_plural = _("Risk Indications")


class Chemical(models.Model):
    """ The Chemical is the heart of this application."""

    name = models.CharField(max_length=200, verbose_name=_("Chemical"))
    comment = models.CharField(max_length=800, blank=True, null=True)
    article = models.CharField(max_length=100, blank=True, null=True)
    registration_number = models.CharField(
        max_length=100, blank=True, null=True)
    cas = models.CharField(max_length=100, blank=True, null=True)
    einecs = models.CharField(max_length=100, blank=True, null=True)

    # Boolean switches
    cmr = models.BooleanField(default=False)
    needed = models.BooleanField(default=False)
    preparation = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    instruction = models.BooleanField(default=False)
    hazardous = models.BooleanField(default=False)
    reach_vo = models.BooleanField(default=False)
    components_registered = models.BooleanField(default=False)

    # Many to many relations
    wgk = models.ManyToManyField(WGK, blank=True)
    synonyms = models.ManyToManyField(Synonym, blank=True)
    storage_classes = models.ManyToManyField(
        StorageClass, blank=True, verbose_name=_("Storage Classes"))
    seveso_categories = models.ManyToManyField(SevesoCategory, blank=True)
    rphrases = models.ManyToManyField(RPhrase, blank=True)
    pphrases = models.ManyToManyField(PPhrase, blank=True)

    # Many to many relations with dedicated relation table
    risks = models.ManyToManyField(
        RiskIndication, through='Risk', blank=True,
        verbose_name=_("Risk Indication"))
    hphrases = models.ManyToManyField(
        HPhrase, through='HPhraseRelation', blank=True)
    departments = models.ManyToManyField(
        'Department', through='Supplier', blank=True)
    pictograms = models.ManyToManyField(
        'Pictogram', through='Signal', blank=True, verbose_name=_("Pictogram"))
    locations = models.ManyToManyField(
        'Location', through='Stock', blank=True)

    def get_approval_documents(self):
        return self.document_set.filter(doctype="FREIGABE")

    def get_info_documents(self):
        return self.document_set.filter(doctype="STOFFINFO")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chemical_detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Chemical")
        verbose_name_plural = _("Chemicals")


class Toxdata(models.Model):
    """Class for Tox / Oekotox information belonging to a chemical."""

    chemical = models.ForeignKey(Chemical)
    supplier = models.ForeignKey('Contact')
    tox = models.BooleanField(default=False)
    oekotox = models.BooleanField(default=False)

    def __unicode__(self):
        return self.supplier.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Tox Oekotox")
        verbose_name_plural = _("Tox Oekotox")


class ReachInformation(models.Model):
    """Class for REACH information belonging to a chemical."""

    chemical = models.ForeignKey(Chemical)
    description = models.TextField()

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Reach Information")
        verbose_name_plural = _("Reach Information")


class SevesoInformation(models.Model):
    """Class for the Seveso information of a chemical."""

    chemical = models.ForeignKey(Chemical)
    description = models.TextField()

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Seveso Information")
        verbose_name_plural = _("Seveso Information")


class Risk(models.Model):
    """Simple class for the risk class of a chemical."""

    chemical = models.ForeignKey(Chemical)
    riskindication = models.ForeignKey(RiskIndication)
    info = models.TextField()

    def __unicode__(self):
        return self.riskindication.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Risk")
        verbose_name_plural = _("Risks")


class HPhraseRelation(models.Model):
    """Simple class for H phrases of a chemical."""

    chemical = models.ForeignKey(Chemical)
    hphrase = models.ForeignKey(HPhrase)
    info = models.TextField(blank=True)

    def __unicode__(self):
        return self.hphrase.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("H-Phrase Relation")
        verbose_name_plural = _("H-Phrase Relations")


#############################################################################
# The following classes contain media objects and will be migrated later
#############################################################################
class Pictogram(models.Model):
    """Class for the pictograms related to a chemical."""

    code = models.CharField(max_length=100)
    name = models.CharField(max_length=400, verbose_name=_("Pictogram"))
    image = FilerImageField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Pictogram")
        verbose_name_plural = _("Pictograms")


class Signal(models.Model):
    """Class mapping chemicals and pictograms and adding a signal words."""

    TERMS = (('d', _('danger')), ('w', _('warning')), ('n', _('no signal')),)

    chemical = models.ForeignKey(Chemical)
    pictogram = models.ForeignKey(Pictogram)
    term = models.CharField(max_length=1, choices=TERMS)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Singal")
        verbose_name_plural = _("Singals")


class Document(models.Model):
    """Class for documents belonging to a chemical."""

    plant = models.ForeignKey('Plant')
    chemical = models.ForeignKey(Chemical)
    file = FilerFileField(null=True, blank=True)
    doctype = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")


class ReachDocument(models.Model):
    """Class for REACH documents belonging to a chemical."""

    chemical = models.ForeignKey(Chemical)
    file = FilerFileField(null=True, blank=True)
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES)
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Reach Document")
        verbose_name_plural = _("Reach Documents")


class SevesoDocument(models.Model):
    """Class for the Seveso document belonging to a chemical.

    Currently there are no elements in this table, therefore it doesn't appear
    in the EER diagram.

    """

    chemical = models.ForeignKey(Chemical)
    file = FilerFileField(null=True, blank=True)
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES)
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Seveso Document")
        verbose_name_plural = _("Seveso Documents")


class SafetyDataSheet(models.Model):
    """Class for safety data sheets belonging to a chemical."""

    supplier = models.ForeignKey('Contact')
    chemical = models.ForeignKey(Chemical)
    file = FilerFileField(null=True, blank=True)
    instruction = models.BooleanField(default=False)
    issue_date = models.DateField(null=True, blank=True)
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES)
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Safety Data Sheet")
        verbose_name_plural = _("Safety Data Sheets")


class ExtendedSafetyDataSheet(models.Model):
    """Class for extended safety data sheets belonging to a chemical."""

    supplier = models.ForeignKey('Contact')
    chemical = models.ForeignKey(Chemical)
    file = FilerFileField(null=True, blank=True)
    instruction = models.BooleanField(default=False)
    issue_date = models.DateField(null=True, blank=True)
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES)
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Extended Safety Data Sheet")
        verbose_name_plural = _("Extended Safety Data Sheets")
