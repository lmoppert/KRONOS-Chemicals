

""" Menu for the chemicals application. """


from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from django.utils.translation import ugettext_lazy as _


class ChemicalMenu(CMSAttachMenu):

    """ Provides the menu. """

    name = _("Substances Menu")

    def get_nodes(self, request):
        """ Return the list of nodes for the menu. """

        nodes = []
        # Categories
        nodes.append(NavigationNode(_('Substance Portal'), "/sicherheitsportal/stoffeportal/", 1))
        nodes.append(NavigationNode(_('Substance Views'), "/sicherheitsportal/stoffeportal/chemicals/", 11, 1))
        nodes.append(NavigationNode(_('SHE Views'), "/sicherheitsportal/stoffeportal/SHE/", 12, 1))
        nodes.append(NavigationNode(_('Stock Views'), "/sicherheitsportal/stoffeportal/Stocks/", 13, 1))
        # Entries for the Substance View
        nodes.append(NavigationNode(_('Substances'), "/substances/", 101, 11))
        nodes.append(NavigationNode(_('Suppliers'), "/suppliers/", 102, 11))
        nodes.append(NavigationNode(_('Producers'), "/producers/", 103, 11))
        nodes.append(NavigationNode(_('Departments'), "/departments/", 104, 11))
        nodes.append(NavigationNode(_('CMR'), "/cmr/", 105, 11))
        nodes.append(NavigationNode(_('Archive'), "/substances/archive/", 106, 11))
        nodes.append(NavigationNode(_('Safetydatasheets'), "/sds/", 107, 11))
        nodes.append(NavigationNode(_('Approval Documents'), "/approval/", 108, 11))
        # Entries for the SHE View
        nodes.append(NavigationNode(_('H-Phrases'), "/hphrases/", 201, 12))
        nodes.append(NavigationNode(_('Substances without SDS'), "/substances/nosds/", 202, 12))
        nodes.append(NavigationNode(_('Seveso-View Departments'), "/seveso/departments/", 203, 12))
        nodes.append(NavigationNode(_('Seveso-View'), "/seveso/", 204, 12))
        nodes.append(NavigationNode(_('Seveso-View Listed Substances'), "/seveso/listed/", 205, 12))
        nodes.append(NavigationNode(_('Checklists'), "/checklists/", 206, 12))
        nodes.append(NavigationNode(_('Tox Oekotox'), "/tox/", 207, 12))
        nodes.append(NavigationNode(_('Substance numbers'), "/subnumber/", 208, 12))
        # Entries for the Stock View
        nodes.append(NavigationNode(_('Departments'), "/stock/departments/", 301, 13))
        nodes.append(NavigationNode(_('Location'), "/stock/location/", 302, 13))
        nodes.append(NavigationNode(_('Substances'), "/stock/substances/", 303, 13))
        nodes.append(NavigationNode(_('Checklists'), "/stock/checklists/", 304, 13))
        return nodes


menu_pool.register_menu(ChemicalMenu)
