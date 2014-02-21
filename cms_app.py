""" App Hook for the substance portal. """

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import ChemicalMenu


class SubstanceApphook(CMSApp):
    name = _("Substance Portal")
    urls = ["chemicals.urls"]
    menus = [ChemicalMenu]

apphook_pool.register(SubstanceApphook)
