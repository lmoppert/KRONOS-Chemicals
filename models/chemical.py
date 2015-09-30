"""Models that are related to a chemical."""

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.utils.translation import ugettext_lazy as _
from polymorphic import PolymorphicModel, PolymorphicManager


class HPhrase(models.Model):
    """Simple class for storing H phrases of a chemical. This also contains
    information about Seveso relevance and CMR value."""

    CMR = (
        (1, _('CMR Category 1A/1B')),
        (2, _('CMR Category 2')),
        (9, _('Not CMR relevant')),
    )
    name = models.CharField(max_length=40, verbose_name=_("H-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))
    seveso_relevant = models.BooleanField(default=False,
                                          verbose_name=_("Seveso Relevant"))
    cmr = models.IntegerField(default=9, choices=CMR, verbose_name=_("CMR"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("H-Phrase")
        verbose_name_plural = _("H-Phrases")


class PPhrase(models.Model):
    """Simple class for storing P phrases of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("P-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("P-Phrase")
        verbose_name_plural = _("P-Phrases")


class RPhrase(models.Model):
    """Simple class for storing R phrases of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("R-Phrase"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("R-Phrase")
        verbose_name_plural = _("R-Phrases")


class SevesoCategory(models.Model):
    """Class for the Seveso category of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("Seveso Category"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Seveso Category")
        verbose_name_plural = _("Seveso Categories")


class StorageClass(models.Model):
    """Class for the storage class of a chemical."""

    name = models.CharField(max_length=40, verbose_name=_("Storage Class"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Storage Class")
        verbose_name_plural = _("Storage Classes")


class WGK(models.Model):
    """Simple class for storing the WGK of a chemical."""

    name = models.CharField(max_length=20, verbose_name=_("WGK"))
    description = models.CharField(max_length=400, blank=True, null=True,
                                   verbose_name=_("Description"))

    def __unicode__(self):
        return "%s - %s" % (self.name, self.description)

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("WGK")
        verbose_name_plural = _("WGKs")


class RiskIndication(models.Model):
    """Simple class for the risk class of a chemical."""

    name = models.CharField(max_length=100, verbose_name=_("Risk"))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Risk Indication")
        verbose_name_plural = _("Risk Indications")


class Chemical(models.Model):
    """The Chemical is the heart of this application."""
    SIGNALS = (('d', _('danger')), ('w', _('warning')), ('n', _('no signal')),)

    comment = models.TextField(verbose_name=_("Comment"), blank=True,
                               default='')
    article = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name=_("Article Number"))
    registration_number = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name=_("Registration Number")
    )
    cas = models.CharField(max_length=100, blank=True, null=True,
                           verbose_name=_("CAS"))
    einecs = models.CharField(max_length=100, blank=True, null=True,
                              verbose_name=_("EINECS"))
    signal = models.CharField(max_length=1, choices=SIGNALS, blank=True,
                              default='', verbose_name=_("Signal"))

    # Boolean switches
    region_de = models.BooleanField(default=True, verbose_name=_("Region D"))
    region_be = models.BooleanField(default=False, verbose_name=_("Region B"))
    archive = models.BooleanField(default=False, verbose_name=_("Archive"))
    needed = models.BooleanField(default=False,
                                 verbose_name=_("Permanently Needed"))
    preparation = models.BooleanField(default=False,
                                      verbose_name=_("Preparation"))
    components_registered = models.BooleanField(
        default=False, verbose_name=_("Components Registered"))
    reach_vo = models.BooleanField(
        default=False, verbose_name=_("Listed in annex XIV REACH regulation"))

    # Many to one relations
    wgk = models.ForeignKey(WGK, default=1, verbose_name=_("WGK"))
    storage_class = models.ForeignKey(StorageClass, default=1,
                                      verbose_name=_("Storage Class"))

    # Many to many relations
    seveso_categories = models.ManyToManyField(
        SevesoCategory, blank=True, verbose_name=_("Seveso Categories"))
    rphrases = models.ManyToManyField(RPhrase, blank=True,
                                      verbose_name=_("R-Phrases"))
    pphrases = models.ManyToManyField(PPhrase, blank=True,
                                      verbose_name=_("P-Phrases"))
    pictograms = models.ManyToManyField('Pictogram', blank=True,
                                        verbose_name=_("Pictogram"))

    # Many to many relations with dedicated relation table
    risks = models.ManyToManyField(RiskIndication, through='Risk', blank=True,
                                   verbose_name=_("Risk Indication"))
    hphrases = models.ManyToManyField(HPhrase, through='HPhraseRelation',
                                      blank=True, verbose_name=_("H-Phrases"))
    locations = models.ManyToManyField('Location', through='Stock', blank=True,
                                       verbose_name=_("Locations"))
    departments = models.ManyToManyField('Department', through='Consumer',
                                         blank=True,
                                         verbose_name=_("Departments"))
    suppliers = models.ManyToManyField('Supplier', through='Consumer',
                                       blank=True,
                                       verbose_name=_("Suppliers"))

    @property
    def cmr1(self):
        if self.hphrases.all().aggregate(models.Min('cmr'))['cmr__min'] == 1:
            return True
        else:
            return False

    @property
    def cmr2(self):
        if self.hphrases.all().aggregate(models.Min('cmr'))['cmr__min'] == 2:
            return True
        else:
            return False

    @property
    def seveso_relevant(self):
        return self.hphrases.filter(seveso_relevant=True).exists()

    def get_approval_documents(self):
        return self.document_set.filter(doctype="f")

    def get_info_documents(self):
        return self.document_set.filter(doctype="i")

    def __unicode__(self):
        return self.name.name

    def get_absolute_url(self):
        return reverse('chemical_detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Chemical")
        verbose_name_plural = _("Chemicals")


class ChemicalName(PolymorphicModel):
    """This only contains the name of the chemicals and synonyms."""
    name = models.CharField(max_length=200, verbose_name=_("Chemical"))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("ChemicalName")
        verbose_name_plural = _("ChemicalNames")


class Identifier(ChemicalName):
    """Class for storing the name of a chemical."""
    chemical = models.OneToOneField(Chemical, default=1, related_name="name",
                                    verbose_name=_("Chemical"))

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Name")
        verbose_name_plural = _("Name")


class Synonym(ChemicalName):
    """Simple Class for storing synonyms of chemicals."""
    chemical = models.ForeignKey(Chemical, default=1, related_name="synonyms",
                                 verbose_name=_("Chemical"))

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Synonym")
        verbose_name_plural = _("Synonyms")


class Toxdata(models.Model):
    """Class for Tox / Oekotox information belonging to a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    supplier = models.ForeignKey('Supplier', verbose_name=_("Supplier"))
    tox = models.BooleanField(default=False, verbose_name=_("Tox"))
    oekotox = models.BooleanField(default=False, verbose_name=_("Oekotox"))

    def __unicode__(self):
        return self.supplier.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Tox Oekotox")
        verbose_name_plural = _("Tox Oekotox")


class ReachInformation(models.Model):
    """Class for REACH information belonging to a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    description = models.TextField(verbose_name=_("Description"), blank=True,
                                   default='')

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Reach Information")
        verbose_name_plural = _("Reach Information")


class SevesoInformation(models.Model):
    """Class for the Seveso information of a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    description = models.TextField(verbose_name=_("Description"), blank=True,
                                   default='')

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Seveso Information")
        verbose_name_plural = _("Seveso Information")


class Risk(models.Model):
    """Simple class for the risk class of a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    riskindication = models.ForeignKey(RiskIndication, verbose_name=_(
                                       "Risk Indication"))
    info = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.riskindication.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Risk")
        verbose_name_plural = _("Risks")


class HPhraseRelation(models.Model):
    """Simple class for H phrases of a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    hphrase = models.ForeignKey(HPhrase, verbose_name=_("H-Phrase"))
    info = models.TextField(blank=True, default='',
                            verbose_name=_("Information"))

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

    code = models.CharField(max_length=100, verbose_name=_("Code"))
    name = models.CharField(max_length=400, verbose_name=_("Pictogram"))
    image = FilerImageField(null=True, blank=True, verbose_name=_("Image"))

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Pictogram")
        verbose_name_plural = _("Pictograms")


class Document(models.Model):
    """Class for documents belonging to a chemical."""

    DOCTYPES = (('f', _('Approval')), ('i', _('Substance Information')))
    plant = models.ForeignKey('Plant')
    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    file = FilerFileField(null=True, blank=True, verbose_name=_("File"))
    doctype = models.CharField(max_length=1, choices=DOCTYPES,
                               verbose_name=_("Document Type"))
    created = models.DateField(blank=True, verbose_name=_("Released on"))

    def __unicode__(self):
        return self.file.label

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")


class ReachDocument(models.Model):
    """Class for REACH documents belonging to a chemical."""

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    file = FilerFileField(null=True, blank=True, verbose_name=_("File"))
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES,
                                    verbose_name=_("Country Code"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created on"))

    def __unicode__(self):
        return self.file.label

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Reach Document")
        verbose_name_plural = _("Reach Documents")


class SevesoDocument(models.Model):
    """Class for the Seveso document belonging to a chemical.

    Currently there are no elements in this table, therefore it doesn't appear
    in the EER diagram.

    """

    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    file = FilerFileField(null=True, blank=True, verbose_name=_("File"))
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES,
                                    verbose_name=_("Country Code"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created on"))

    def __unicode__(self):
        return self.file.label

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Seveso Document")
        verbose_name_plural = _("Seveso Documents")


class SafetyDataSheet(models.Model):
    """Class for safety data sheets belonging to a chemical."""

    supplier = models.ForeignKey('Supplier', verbose_name=_("Supplier"))
    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    file = FilerFileField(null=True, blank=True, verbose_name=_("File"))
    issue_date = models.DateField(null=True, blank=True,
                                  verbose_name=_("Issue Date"))
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES,
                                    verbose_name=_("Country Code"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created on"))

    def __unicode__(self):
        return self.file.label

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Safety Data Sheet")
        verbose_name_plural = _("Safety Data Sheets")


class ExtendedSafetyDataSheet(models.Model):
    """Class for extended safety data sheets belonging to a chemical."""

    supplier = models.ForeignKey('Supplier', verbose_name=_("Supplier"))
    chemical = models.ForeignKey(Chemical, verbose_name=_("Chemical"))
    file = FilerFileField(null=True, blank=True, verbose_name=_("File"))
    issue_date = models.DateField(null=True, blank=True,
                                  verbose_name=_("Issue Date"))
    country_code = models.CharField(max_length=2, choices=settings.LANGUAGES,
                                    verbose_name=_("Country Code"))
    created = models.DateField(auto_now_add=True, verbose_name=_("Created on"))

    def __unicode__(self):
        return self.file.label

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Extended Safety Data Sheet")
        verbose_name_plural = _("Extended Safety Data Sheets")
