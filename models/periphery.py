"""Models that are related to persons, companies or locations."""

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Person(models.Model):
    """Class holding information about a person."""

    title = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name=_("Title"))
    academic_title = models.CharField(max_length=100, blank=True, null=True,
                                      verbose_name=_("Academic Title"))
    surname = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name=_("Surname"))
    givenname = models.CharField(max_length=200, verbose_name=_("Given name"))
    phone = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name=_("Phone"))
    fax = models.CharField(max_length=100, blank=True, null=True,
                           verbose_name=_("Fax"))
    email = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name=_("Email"))

    @property
    def name(self):
        return "%s %s" % (self.surname, self.givenname)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('givenname', 'surname')
        app_label = "chemicals"
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Supplier(models.Model):
    """Class holding information about a company."""

    persons = models.ManyToManyField(Person, through='Role',
                                     verbose_name=_("Persons"))
    name = models.CharField(max_length=400, verbose_name=_("Name"))
    address = models.TextField(blank=True, null=True, verbose_name=_("Address"))
    country = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name=_("Country"))
    phone = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name=_("Phone"))
    fax = models.CharField(max_length=100, blank=True, null=True,
                           verbose_name=_("Fax"))
    email = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name=_("Email"))
    web = models.CharField(max_length=100, blank=True, null=True,
                           verbose_name=_("Web"))
    info = models.TextField(blank=True, null=True,
                            verbose_name=_("Information"))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")


class Role(models.Model):
    """Class determining the role of a person in a company."""

    ROLES = (('r', 'REACH'), ('c', _('Chemical')),)

    # This model was originally named Contact_Person
    person = models.ForeignKey(Person, verbose_name=_("Person"))
    supplier = models.ForeignKey(Supplier, verbose_name=_("Supplier"))
    role = models.CharField(max_length=1, choices=ROLES, verbose_name=_("Role"))

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")


class Plant(models.Model):
    """Class with informations about a production site (LEV, NHM, ...).

    This model was originally named menufacturing

    """

    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Plant")
        verbose_name_plural = _("Plants")


class Department(models.Model):
    """Class with informations about a department in a specific plant."""

    plant = models.ForeignKey(Plant, verbose_name=_("Plant"))
    name = models.CharField(max_length=100, verbose_name=_("Name"),
                            db_index=True)

    def get_absolute_url(self):
        return reverse('department_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        app_label = "chemicals"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Profile(models.Model):
    """Class extending the build in User model."""

    user = models.OneToOneField(User, verbose_name=_("Profile"))
    departments = models.ManyToManyField(Department,
                                         verbose_name=_("Managed Department"))

    def __unicode__(self):
        return self.user.get_full_name()

    class Meta:
        app_label = "chemicals"
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        permissions = (
            ('view_she', "Can see features only visible for SHE members"),
        )


class Location(models.Model):
    """Class naming a storage room of a specific department."""

    department = models.ForeignKey(Department, verbose_name=_("Department"))
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock_location_list', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        app_label = "chemicals"
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class Stock(models.Model):
    """Class adding volume informatino for a chemical to a location."""
    UNITS = {'p': 'units', 't': 't', 'l': 'l', 'g': 'g', 'c': 'm3', 'k': 'kg',
             'm': 'ml'}
    UNIT_CHOICES = (
        ('t', _('tons')), ('k', _('kilogram')), ('g', _('gram')),
        ('c', _('cubic meter')), ('l', _('liter')), ('m', _('mililiter')),
        ('p', _('pieces')),
    )

    chemical = models.ForeignKey('Chemical', verbose_name=_("Chemical"))
    location = models.ForeignKey(Location, verbose_name=_("Location"))
    max_volume = models.CharField(
        max_length=25, blank=True, null=True, verbose_name=_("Volume"))
    max_unit = models.CharField(
        max_length=1, choices=UNIT_CHOICES, verbose_name=_("Unit"))
    year_volume = models.CharField(
        max_length=25, blank=True, null=True, verbose_name=_("Year Volume"))
    year_unit = models.CharField(
        max_length=1, choices=UNIT_CHOICES, verbose_name=_("Unit"))

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")


class Consumer(models.Model):
    """Class mapping a chemical with a department and a supplier."""

    chemical = models.ForeignKey('Chemical', verbose_name=_("Chemical"))
    department = models.ForeignKey(Department, verbose_name=_("Department"))
    supplier = models.ForeignKey(Supplier, verbose_name=_("Supplier"))
    comment = models.TextField(verbose_name=_("Comment"), blank=True,
                               default='')

    @property
    def stocks(self):
        return self.chemical.stock_set.filter(
            location__in=self.department.location_set.all())

    def __unicode__(self):
        return u"{} | {} | {}".format(
            self.chemical,
            self.department,
            self.supplier
        )

    class Meta:
        app_label = "chemicals"
        verbose_name = _("Consumer")
        verbose_name_plural = _("Consumers")
