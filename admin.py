"""Admin configuration for the chemicals application."""

# pep257: disable C0110

from chemicals import models
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.utils.translation import ugettext_lazy as _


##############################################################################
# Admin of Chemicals
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

    filter_horizontal = ('wgk', 'storage_classes', 'seveso_categories',
                         'rphrases', )


##############################################################################
# Admin of Contacts
##############################################################################
class RoleInline(admin.TabularInline):
    """Inline view for a role."""

    model = models.Role
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
#    model = models.UserProfile
#    max_num = 1
#    can_delete = False


admin.site.register(models.RiskIndication, RiskIndicationAdmin)
admin.site.register(models.WGK, WGKAdmin)
admin.site.register(models.StorageClass, StorageClassAdmin)
admin.site.register(models.SevesoCategory, SevesoCategoryAdmin)
admin.site.register(models.RPhrase, RPhraseAdmin)
admin.site.register(models.PPhrase, PPhraseAdmin)
admin.site.register(models.HPhrase, HPhraseAdmin)
admin.site.register(models.Chemical, ChemicalAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Plant, PlantAdmin)
# admin.site.register(models.CheckList, CheckListAdmin)
