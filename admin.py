"""Admin configuration for the chemicals application."""

# pep257: disable C0110

from chemicals import models
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.utils.translation import ugettext_lazy as _


##############################################################################
# Inline definitions for Chemicals
##############################################################################
class DepartmentInline(admin.TabularInline):
    """Inline view for the departments."""

    model = models.Chemical.departments.through
    extra = 0
    suit_classes = 'suit-tab suit-tab-department'


class DocumentInline(admin.TabularInline):
    """Inline view for the documents."""

    model = models.Document
    extra = 0
    suit_classes = 'suit-tab suit-tab-sds'


class ReachDocumentInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.ReachDocument
    extra = 0
    suit_classes = 'suit-tab suit-tab-reach'


class ReachInformationInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = models.ReachInformation
    extra = 0
    suit_classes = 'suit-tab suit-tab-reach'


class SafetyDataSheetInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.SafetyDataSheet
    extra = 0
    suit_classes = 'suit-tab suit-tab-sds'


class ExtendedSafetyDataSheetInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.ExtendedSafetyDataSheet
    extra = 0
    suit_classes = 'suit-tab suit-tab-sds'


class SevesoDocumentInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.SevesoDocument
    extra = 0
    suit_classes = 'suit-tab suit-tab-seveso'


class SevesoInformationInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = models.SevesoInformation
    extra = 0
    suit_classes = 'suit-tab suit-tab-seveso'


##############################################################################
# Admin of Chemicals
##############################################################################
@admin.register(models.RiskIndication)
class RiskIndicationAdmin(TranslationAdmin):
    """Admin view for Risk Indications."""

    list_display = ('name',)
    search_fields = ('name', )


@admin.register(models.WGK)
class WGKAdmin(TranslationAdmin):
    """Admin view for WGK."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.StorageClass)
class StorageClassAdmin(TranslationAdmin):
    """Admin view for Storage Classes."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.SevesoCategory)
class SevesoCategoryAdmin(TranslationAdmin):
    """Admin view for Seveso Categories."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.RPhrase)
class RPhraseAdmin(TranslationAdmin):
    """Admin view for R-Phrases."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.PPhrase)
class PPhraseAdmin(TranslationAdmin):
    """Admin view for R-Phrases."""

    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(models.HPhrase)
class HPhraseAdmin(TranslationAdmin):
    """Admin view for H-Phrases."""

    list_display = ('name', 'description', 'cmr', 'seveso_relevant')
    search_fields = ('name', 'description')


@admin.register(models.Chemical)
class ChemicalAdmin(TranslationAdmin):
    """Admin view for the chemicals."""

    list_display = ('name', 'registration_number', 'article', 'comment')
    search_fields = ('name', )
    list_filter = ('preparation', 'archive', 'signal', 'hphrases__cmr')
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('name', 'synonyms',)
        }),
        (_('Values'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('article', 'registration_number', 'cas',
                       'einecs',)
        }),
        (_('Flags'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('needed', 'preparation', 'archive', 'reach_vo',
                       'components_registered')
        }),
        (_('Relations'), {
            'classes': ('suit-tab', 'suit-tab-classification', ),
            'fields': ('wgk', 'storage_classes', 'rphrases', 'signal')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seveso',),
            'fields': ('seveso_categories', )
        }),
        (_('Comments'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('comment',)
        }),
    )
    filter_horizontal = ('seveso_categories', 'rphrases',)
    suit_form_tabs = (
        ('general', _('Identification')),
        ('classification', _('Classification')),
        ('department', _('Department / Supplier')),
        ('sds', _('SDS / Documents')),
        ('reach', _('REACH')),
        ('checklist', _('Checklists')),
        ('seveso', _('Seveso')),
    )
    inlines = [
        DepartmentInline,
        DocumentInline,
        ReachDocumentInline,
        ReachInformationInline,
        SafetyDataSheetInline,
        ExtendedSafetyDataSheetInline,
        SevesoDocumentInline,
        SevesoInformationInline,
    ]


@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):
    """Admin view for the Stock Locations."""

    list_display = ('chemical', 'location')
    search_fields = ['chemical__name', 'location__name']


##############################################################################
# Admin of Contacts
##############################################################################
class RoleInline(admin.TabularInline):
    """Inline view for a role."""

    model = models.Role
    extra = 1


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin view for a person."""

    list_display = ('title', 'academic_title', 'surname', 'givenname')
    list_display_links = ('surname', 'givenname')
    search_fields = ('surname', 'givenname', 'title')
    inlines = [
        RoleInline,
    ]


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin view for the contacts."""

    list_display = ('name', 'country', 'info')
    search_fields = ('name', 'info', )
    inlines = [
        RoleInline,
    ]


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin view for a supplier."""

    list_display = ('department', 'chemical', 'contact')
    search_fields = ('department', 'chemical', 'contact')


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Admin view for a department."""

    list_display = ('name', 'plant')
    search_fields = ('name', )


@admin.register(models.Plant)
class PlantAdmin(TranslationAdmin):
    """Admin view for a department."""

    list_display = ('name',)
    search_fields = ('name', )


##############################################################################
# Admin of Checklists
##############################################################################
class CheckSectionInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = models.CheckSection
    extra = 1


class HPhraseCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.HPhraseCheck
    extra = 1


class PPhraseCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.PPhraseCheck
    extra = 1


class WGKCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.WGKCheck
    extra = 1


class PictogramCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.PictogramCheck
    extra = 1


class StorageClassCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.StorageClassCheck
    extra = 1


class PPECheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = models.PPECheck
    extra = 1


# @admin.register(models.CheckList)
class CheckListAdmin(admin.ModelAdmin):
    """Admin view for the check list."""

    list_display = ('chemical', 'department', 'country_code', 'status')
    inlines = [
        CheckSectionInline,
        HPhraseCheckInline,
        PPhraseCheckInline,
        WGKCheckInline,
        PictogramCheckInline,
        StorageClassCheckInline,
        PPECheckInline,
    ]


# class UserProfileInline(admin.StackedInline):
#    """Inline view for the user profile."""
#
#    model = models.UserProfile
#    max_num = 1
#    can_delete = False
