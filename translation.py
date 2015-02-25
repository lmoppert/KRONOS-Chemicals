""" Model Translations for Chemicals."""

from modeltranslation.translator import translator, TranslationOptions
from .models.chemical import (HPhrase, PPhrase, RPhrase, Pictogram, WGK, Risk,
                               SevesoCategory, StorageClass, ReachInformation,
                               SevesoInformation, Chemical, Synonym,
                               RiskIndication, HPhraseRelation)
from .models.periphery import Plant
from .models.checklist import CheckUsage, CheckSection, PPE


class NameTranslationOptions(TranslationOptions):

    """Translating only the name field."""

    fields = ('name',)


translator.register(Plant, NameTranslationOptions)
translator.register(Pictogram, NameTranslationOptions)
translator.register(Synonym, NameTranslationOptions)
translator.register(RiskIndication, NameTranslationOptions)


class DescriptionTranslationOptions(TranslationOptions):

    """Translating only the description field."""

    fields = ('description',)


translator.register(StorageClass, DescriptionTranslationOptions)
translator.register(ReachInformation, DescriptionTranslationOptions)
translator.register(SevesoInformation, DescriptionTranslationOptions)
translator.register(CheckUsage, DescriptionTranslationOptions)
translator.register(CheckSection, DescriptionTranslationOptions)
translator.register(PPE, DescriptionTranslationOptions)
translator.register(WGK, DescriptionTranslationOptions)
translator.register(SevesoCategory, DescriptionTranslationOptions)
translator.register(HPhrase, DescriptionTranslationOptions)
translator.register(PPhrase, DescriptionTranslationOptions)
translator.register(RPhrase, DescriptionTranslationOptions)


class InfoTranslationOptions(TranslationOptions):

    """Translating only the info field."""

    fields = ('info',)


translator.register(Risk, InfoTranslationOptions)
translator.register(HPhraseRelation, InfoTranslationOptions)


class ChemicalTranslationOptions(TranslationOptions):

    """Translating both, name and comment field."""

    fields = ('name', 'comment',)


translator.register(Chemical, ChemicalTranslationOptions)
