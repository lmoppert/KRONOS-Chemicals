"""Models that are related to persons, companies or locations."""

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    """Class holding information about a person."""

    title = models.CharField(max_length=100, blank=True, null=True)
    academic_title = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    givenname = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def _get_name(self):
        return "%s %s" % (self.surname, self.givenname)
    name = property(_get_name)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Contact(models.Model):
    """Class holding information about a company."""

    persons = models.ManyToManyField(Person, through='Role')
    name = models.CharField(max_length=400)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('contact_detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Role(models.Model):
    """Class determining the role of a person in a company."""

    ROLES = (('r', 'REACH'), ('c', _('Chemical')),)

    # This model was originally named Contact_Person
    person = models.ForeignKey(Person)
    contact = models.ForeignKey(Contact)
    role = models.CharField(max_length=1, choices=ROLES)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")


class Plant(models.Model):
    """Class with informations about a production site (LEV, NHM, ...).

    This model was originally named menufacturing

    """

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Plant")
        verbose_name_plural = _("Plants")


class Department(models.Model):
    """Class with informations about a department in a specific plant."""

    plant = models.ForeignKey(Plant)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")
        ordering = ['name']


class Location(models.Model):
    """Class naming a storage room of a specific department."""

    department = models.ForeignKey(Department)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('location_detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class Stock(models.Model):
    """Class adding volume informatino for a chemical to a location."""

    UNITS = (
        ('t', _('tons')), ('k', _('kilogram')), ('g', _('gram')),
        ('c', _('cubic meter')), ('l', _('liter')), ('m', _('mililiter')),
        ('p', _('pieces')),
    )

    chemical = models.ForeignKey('Chemical')
    location = models.ForeignKey(Location)
    max_volume = models.CharField(
        max_length=25, blank=True, null=True, verbose_name=_("Volume"))
    max_unit = models.CharField(
        max_length=1, choices=UNITS, verbose_name=_("Unit"))
    year_volume = models.CharField(
        max_length=25, blank=True, null=True, verbose_name=_("Year Volume"))
    year_unit = models.CharField(
        max_length=1, choices=UNITS, verbose_name=_("Unit"))

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")


class Supplier(models.Model):
    """Class mapping a supplier of a chemical with a department."""

    chemical = models.ForeignKey('Chemical')
    contact = models.ForeignKey(Contact)
    department = models.ForeignKey(Department)
    has_instructions = models.BooleanField(default=False, null=False)

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")
