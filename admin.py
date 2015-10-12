"""Admin configuration for the chemicals application."""

# pep257: disable C0110

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.utils.translation import ugettext_lazy as _
from chemicals import models


##############################################################################
# Inline definitions for Chemicals
##############################################################################
class DepartmentInline(admin.TabularInline):
    """Inline view for the departments."""

    model = models.Consumer
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


class HPhraseInline(TranslationTabularInline):
    """Inline view for the hphrases."""

    model = models.HPhraseRelation
    extra = 0
    suit_classes = 'suit-tab suit-tab-classification'


class RiskInline(TranslationTabularInline):
    """Inline view for the risks."""

    model = models.Risk
    extra = 0
    suit_classes = 'suit-tab suit-tab-classification'


class ToxInline(admin.TabularInline):
    """Inline view for the tox / oekotox."""

    model = models.Toxdata
    extra = 0
    suit_classes = 'suit-tab suit-tab-classification'


class SynonymInline(admin.TabularInline):
    """Inline view for the synonyms of a chemical."""

    model = models.Synonym
    fk_name = 'chemical'
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


class IdentifierInline(admin.TabularInline):
    """Inline view for the synonyms of a chemical."""

    model = models.Identifier
    can_delete = False
    fk_name = 'chemical'
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


##############################################################################
# Admin of Chemicals
##############################################################################
@admin.register(models.Pictogram)
class PictogramAdmin(TranslationAdmin):
    """Admin view for Pictograms."""

    list_display = ('name', 'code')
    search_fields = ('name', 'code')


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

    list_display = ('name', 'preparation', 'article', 'cas', 'einecs',
                    'archive')
    search_fields = ('name__name', 'article', 'cas', 'einecs',
                     'registration_number')
    list_filter = ('preparation', 'archive', 'hphrases', 'hphrases__cmr', 'wgk',
                   'storage_class', 'toxdata__tox', 'toxdata__oekotox',
                   'region_de', 'region_be')
    actions = ('archive_chemicals', 'unarchive_chemicals')
    fieldsets = (
        (_('Regions'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('region_de', 'region_be')
        }),
        (_('Values'), {
            'classes': ('suit-tab', 'suit-tab-identification',),
            'fields': ('article', 'registration_number', 'cas',
                       'einecs',)
        }),
        (_('Flags'), {
            'classes': ('suit-tab', 'suit-tab-identification',),
            'fields': ('needed', 'preparation', 'archive', 'reach_vo',
                       'components_registered')
        }),
        (_('Relations'), {
            'classes': ('suit-tab', 'suit-tab-classification', ),
            'fields': ('wgk', 'storage_class', 'pictograms', 'signal',
                       'rphrases')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seveso',),
            'fields': ('seveso_categories', )
        }),
        (_('Comments'), {
            'classes': ('suit-tab', 'suit-tab-identification',),
            'fields': ('comment',)
        }),
    )
    filter_horizontal = ('seveso_categories', 'rphrases', 'pictograms')
    suit_form_tabs = (
        ('general', _('Names')),
        ('identification', _('Identification')),
        ('classification', _('Classification')),
        ('department', _('Department / Supplier')),
        ('sds', _('SDS / Documents')),
        ('reach', _('REACH')),
        ('checklist', _('Checklists')),
        ('seveso', _('Seveso')),
    )
    inlines = (
        IdentifierInline,
        SynonymInline,
        DepartmentInline,
        DocumentInline,
        ReachDocumentInline,
        ReachInformationInline,
        SafetyDataSheetInline,
        ExtendedSafetyDataSheetInline,
        SevesoDocumentInline,
        SevesoInformationInline,
        HPhraseInline,
        RiskInline,
        ToxInline,
    )

    def archive_chemicals(self, request, queryset):
        queryset.update(archive=True)
    archive_chemicals.short_description = _(
        "Move selected chemicals to archive")

    def unarchive_chemicals(self, request, queryset):
        queryset.update(archive=False)
    unarchive_chemicals.short_description = _(
        "Remove selected chemicals from archive")


##############################################################################
# Admin of Authentication
##############################################################################
admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    """Inline view for the department admins used for User Form."""

    model = models.Profile
    can_delete = False
    suit_classes = 'suit-tab suit-tab-general'
    filter_horizontal = ('departments',)
    verbose_name = _("managed department")
    verbose_name_plural = _("managed departments")


class ManagersInline(admin.TabularInline):
    """Inline view for the admins of a department."""

    model = models.Profile.departments.through
    extra = 0
    verbose_name = _("department admin")
    verbose_name_plural = _("department admins")


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('username', 'password', 'first_name', 'last_name',
                       'email')
        }),
        (_('Permissions'), {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('User permissions'), {
            'classes': ('suit-tab', 'suit-tab-extended',),
            'fields': ('groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'classes': ('suit-tab', 'suit-tab-extended',),
            'fields': ('last_login', 'date_joined')
        }),
    )
    suit_form_tabs = (
        ('general', _('General')),
        ('extended', _('Extended')),
    )
    inlines = (ProfileInline, )


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
    inlines = (RoleInline, )


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin view for the suppliers."""

    list_display = ('name', 'country', 'info')
    search_fields = ('name', 'info', )
    inlines = (RoleInline, )


class LocationInline(admin.TabularInline):
    """Inline view for the locations of a department."""

    model = models.Location
    extra = 0


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Admin view for a department."""

    list_display = ('name', 'plant')
    search_fields = ('name', )
    list_filter = ('plant', )
    inlines = (LocationInline, ManagersInline)


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
# class CheckListAdmin(admin.ModelAdmin):
#     """Admin view for the check list."""
#
#     list_display = ('chemical', 'department', 'country_code', 'status')
#     inlines = [
#         CheckSectionInline,
#         HPhraseCheckInline,
#         PPhraseCheckInline,
#         WGKCheckInline,
#         PictogramCheckInline,
#         StorageClassCheckInline,
#         PPECheckInline,
#     ]
