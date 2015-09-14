""" Model Translations for Chemicals."""

from modeltranslation.translator import translator, TranslationOptions
from chemicals import models


class NameTranslationOptions(TranslationOptions):
    """Translating only the name field."""
    fields = ('name',)


translator.register(models.Plant, NameTranslationOptions)
translator.register(models.Pictogram, NameTranslationOptions)
translator.register(models.RiskIndication, NameTranslationOptions)
translator.register(models.ChemicalName, NameTranslationOptions)


class DescriptionTranslationOptions(TranslationOptions):
    """Translating only the description field."""
    fields = ('description',)


translator.register(models.StorageClass, DescriptionTranslationOptions)
translator.register(models.ReachInformation, DescriptionTranslationOptions)
translator.register(models.SevesoInformation, DescriptionTranslationOptions)
translator.register(models.CheckUsage, DescriptionTranslationOptions)
translator.register(models.CheckSection, DescriptionTranslationOptions)
translator.register(models.PPE, DescriptionTranslationOptions)
translator.register(models.WGK, DescriptionTranslationOptions)
translator.register(models.SevesoCategory, DescriptionTranslationOptions)
translator.register(models.HPhrase, DescriptionTranslationOptions)
translator.register(models.PPhrase, DescriptionTranslationOptions)
translator.register(models.RPhrase, DescriptionTranslationOptions)


class InfoTranslationOptions(TranslationOptions):
    """Translating only the info field."""
    fields = ('info',)


translator.register(models.Risk, InfoTranslationOptions)
translator.register(models.HPhraseRelation, InfoTranslationOptions)


class CommentTranslationOptions(TranslationOptions):
    """Translating both, name and comment field."""
    fields = ('comment',)


translator.register(models.Chemical, CommentTranslationOptions)
translator.register(models.Synonym)
translator.register(models.Identifier)
