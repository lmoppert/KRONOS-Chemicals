"""Admin configuration for the chemicals application."""

# pep257: disable C0110

from chemicals.models import (Chemical, Document, ReachDocument,
                              ReachInformation, SafetyDataSheet,
                              ExtendedSafetyDataSheet, SevesoDocument,
                              SevesoInformation, Signal, CheckList,
                              CheckSection, HPhraseCheck, PPhraseCheck,
                              WGKCheck, PictogramCheck, StorageClassCheck,
                              PPECheck, Contact, Role, Person, Supplier,
                              Department, Plant, RiskIndication, WGK,
                              StorageClass, SevesoCategory, RPhrase, PPhrase,
                              HPhrase
                              )
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.utils.translation import ugettext_lazy as _


##############################################################################
# Admin of Chemicals
##############################################################################
class DepartmentInline(admin.TabularInline):
    """Inline view for the departments."""

    model = Chemical.departments.through
    extra = 0
    suit_classes = 'suit-tab suit-tab-department'


class DocumentInline(admin.TabularInline):
    """Inline view for the documents."""

    model = Document
    extra = 1
    suit_classes = 'suit-tab suit-tab-sds'


class ReachDocumentInline(admin.TabularInline):
    """Inline view for the risks."""

    model = ReachDocument
    extra = 1
    suit_classes = 'suit-tab suit-tab-reach'


class ReachInformationInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = ReachInformation
    extra = 0
    suit_classes = 'suit-tab suit-tab-reach'


class SafetyDataSheetInline(admin.TabularInline):
    """Inline view for the risks."""

    model = SafetyDataSheet
    extra = 1
    suit_classes = 'suit-tab suit-tab-sds'


class ExtendedSafetyDataSheetInline(admin.TabularInline):
    """Inline view for the risks."""

    model = ExtendedSafetyDataSheet
    extra = 1
    suit_classes = 'suit-tab suit-tab-sds'


class SevesoDocumentInline(admin.TabularInline):
    """Inline view for the risks."""

    model = SevesoDocument
    extra = 1
    suit_classes = 'suit-tab suit-tab-seveso'


class SevesoInformationInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = SevesoInformation
    extra = 0
    suit_classes = 'suit-tab suit-tab-seveso'


class SignalInline(admin.TabularInline):
    """Inline view for the risks."""

    model = Signal
    extra = 1
    suit_classes = 'suit-tab suit-tab-classification'


class RiskIndicationAdmin(TranslationAdmin):
    """Admin view for Risk Indications."""

    list_display = ('name',)


class WGKAdmin(TranslationAdmin):
    """Admin view for WGK."""

    list_display = ('name', 'description')


class StorageClassAdmin(TranslationAdmin):
    """Admin view for Storage Classes."""

    list_display = ('name', 'description')


class SevesoCategoryAdmin(TranslationAdmin):
    """Admin view for Seveso Categories."""

    list_display = ('name', 'description')


class RPhraseAdmin(TranslationAdmin):
    """Admin view for R-Phrases."""

    list_display = ('name', 'description')


class PPhraseAdmin(TranslationAdmin):
    """Admin view for R-Phrases."""

    list_display = ('name', 'description')


class HPhraseAdmin(TranslationAdmin):
    """Admin view for H-Phrases."""

    list_display = ('name', 'description')


class ChemicalAdmin(TranslationAdmin):
    """Admin view for the chemicals."""

    list_display = ('name', 'registration_number', 'article', 'comment')
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('name', 'synonyms',)
        }),
        (_('Comments'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('comment',)
        }),
        (_('Values'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('article', 'registration_number', 'cas',
                       'einecs', 'replaced',)
        }),
        (_('Flags'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('cmr', 'needed', 'preparation', 'archive',
                       'instruction', 'hazardous', 'reach_vo',
                       'components_registered')
        }),
        (_('Relations'), {
            'classes': ('suit-tab', 'suit-tab-classification', ),
            'fields': ('wgk', 'storage_classes', 'seveso_categories',
                       'rphrases', 'pphrases')
        }),
        (_('Supplier'), {
            'classes': ('suit-tab', 'suit-tab-department', ),
            'fields': ('producer',)
        }),
    )

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
        SignalInline,
    ]

    filter_horizontal = ('storage_classes', 'seveso_categories', 'rphrases',
                         'pphrases', 'producer')


##############################################################################
# Admin of Contacts
##############################################################################
class RoleInline(admin.TabularInline):
    """Inline view for a role."""

    model = Role
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    """Admin view for a person."""

    list_display = ('title', 'academic_title', 'surname', 'givenname')
    inlines = [
        RoleInline,
    ]


class ContactAdmin(admin.ModelAdmin):
    """Admin view for the contacts."""

    list_display = ('name', 'country', 'info')
    inlines = [
        RoleInline,
    ]


class SupplierAdmin(admin.ModelAdmin):
    """Admin view for a supplier."""

    list_display = ('department', 'chemical', 'contact')


class DepartmentAdmin(admin.ModelAdmin):
    """Admin view for a department."""

    list_display = ('name', 'plant')


class PlantAdmin(TranslationAdmin):
    """Admin view for a department."""

    list_display = ('name',)


##############################################################################
# Admin of Checklists
##############################################################################
class CheckSectionInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = CheckSection
    extra = 1


class HPhraseCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = HPhraseCheck
    extra = 1


class PPhraseCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = PPhraseCheck
    extra = 1


class WGKCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = WGKCheck
    extra = 1


class PictogramCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = PictogramCheck
    extra = 1


class StorageClassCheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = StorageClassCheck
    extra = 1


class PPECheckInline(admin.TabularInline):
    """Inline view for the risks."""

    model = PPECheck
    extra = 1


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
#
#    """Inline view for the user profile."""
#
#    model = UserProfile
#    max_num = 1
#    can_delete = False


admin.site.register(RiskIndication, RiskIndicationAdmin)
admin.site.register(WGK, WGKAdmin)
admin.site.register(StorageClass, StorageClassAdmin)
admin.site.register(SevesoCategory, SevesoCategoryAdmin)
admin.site.register(RPhrase, RPhraseAdmin)
admin.site.register(PPhrase, PPhraseAdmin)
admin.site.register(HPhrase, HPhraseAdmin)
admin.site.register(Chemical, ChemicalAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(CheckList, CheckListAdmin)
