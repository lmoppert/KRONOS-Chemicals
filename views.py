# vim: set fileencoding=utf-8 :
"""Views for the substance portal."""

from django.shortcuts import _get_queryset, get_list_or_404
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django_tables2 import SingleTableMixin, RequestConfig
from . import tables, models


###############################################################################
# Custom Generic View Classes
###############################################################################
class TableListMixin(SingleTableMixin):
    """Provides an extra attribute for ListViews."""
    table_heading = ''
    template_name = 'chemicals/table_list.html'
    table_pagination = {'per_page': '25'}
    filters = {'letter': True, 'department': False, 'items': True}
    target_name = "department_detail"

    def get_filter_values(self):
        val = {'letter': '', }
        letters = [False] * 40
        if "lid" in self.request.GET:
            lid = int(self.request.GET["lid"])
            val['letter'] = list(
                "abcdefghijklmnopqrstuvwxyz([_0123456789")[lid - 1]
            letters[lid] = True
        else:
            letters[0] = True
        val['letters'] = letters
        return val

    def get_location_list(self):
        locations = {}
        for plant in get_list_or_404(models.Plant):
            locations[plant.name] = models.Location.objects.filter(
                department__plant=plant.id)
        return locations

    def get_table_heading(self):
        if self.table_heading == '':
            raise ImproperlyConfigured(
                '"table_heading" variable not defined in %s'
                % self.__class__.__name__)
        return self.table_heading

    def get_data_or_dict(self, klass, *args, **kwargs):
        queryset = _get_queryset(klass)
        obj_list = list(queryset.filter(*args, **kwargs)) or []
        return obj_list

    def get_context_data(self, **kwargs):
            context = super(TableListMixin, self).get_context_data(**kwargs)
            context['show_filter'] = self.filters
            context['letters'] = self.get_filter_values()['letters']
            context['plants'] = sorted(
                get_list_or_404(models.Plant), key=lambda x: x.name)
            context['target_name'] = self.target_name
            context['tableheading'] = self.get_table_heading()
            return context


class TableListView(TableListMixin, ListView):
    """Generic View that adds the TableListMixin to the ListView"""


###############################################################################
# Substances Views
###############################################################################
class ChemicalList(TableListView):
    """Returns a list of all Substances that are not archived."""
    model = models.Chemical
    table_class = tables.SubstanceTable
    table_heading = _("Chemicals")
    archive = False

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Chemical, name__istartswith=letter, archive=self.archive,
        )


class ChemicalDetail(DetailView):
    """Returns details about a specific chemical."""
    model = models.Chemical

    def get_context_data(self, **kwargs):
        context = super(ChemicalDetail, self).get_context_data(**kwargs)
        chemical = context["chemical"]
        locations = []
        for supplier in chemical.supplier_set.all():
            locs = supplier.department.location_set.filter(
                stock__in=chemical.stock_set.all())
            for location in locs:
                locations.append({
                    'url': reverse('chemical_department', kwargs={
                        'pk': chemical.id,
                        'dep_id': supplier.department.id, }),
                    'name': location.name,
                    'department': supplier.department.name,
                    'supplier': supplier.contact.name
                })
        context["locations"] = locations
        return context


class SupplierList(TableListView):
    """Returns a list of all Suppliers."""
    model = models.Supplier
    table_class = tables.SupplierTable
    table_heading = _("Suppliers")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Supplier, chemical__archive=False,
            contact__name__istartswith=letter
        )


class CMRList(SupplierList):
    """Returns a list of Suppliers for CMR Chemicals."""
    table_class = tables.CMRTable
    table_heading = _("Suppliers (CMR)")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Supplier, chemical__cmr=True, chemical__archive=False,
            chemical__name__istartswith=letter
        )


class ContactDetail(DetailView):
    """Returns details about a specific contact."""
    model = models.Contact


class DepartmentList(TableListView):
    """Returns the list of departments."""
    model = models.Department
    table_class = tables.DepartmentSubstanceTable
    table_heading = _("Departments")
    filters = {'letter': False, 'department': True}

    def get_table_data(self):
        return []


class DepartmentView(TableListMixin, DetailView):
    """Returns the list of chemicals used in a specific department."""
    model = models.Department
    table_class = tables.DepartmentSubstanceTable
    table_heading = _("Departments")
    filters = {'letter': True, 'department': True}

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_object().chemical_set.filter(
            name__istartswith=letter, archive=False)

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        department = context["department"]
        context['tableheading'] = department.name
        return context


class SDSList(ListView):
    """Returns a list of safety data sheets."""
    model = models.SafetyDataSheet
    table_heading = _("Safety Data Sheets")
    template_name = 'chemicals/sds_list.html'
    filters = {'letter': False, 'department': True}

    def get_context_data(self, **kwargs):
        context = super(SDSList, self).get_context_data(**kwargs)
        table = tables.SDSTable([])
        RequestConfig(
            self.request, paginate={'per_page': '25'}).configure(table)
        context['table'] = table
        context['tableheading'] = _("Safety Data Sheets")
        context['show_filter'] = self.filters
        context['plants'] = sorted(
            get_list_or_404(models.Plant), key=lambda x: x.name)
        context['target_name'] = "department_detail"
        return context


class SDSDepartmentList(DetailView):
    """Returns a list of safety data sheets belonging to a department."""
    model = models.Department
    table_heading = _("Safety Data Sheets")
    template_name = 'chemicals/sds_list.html'
    filters = {'letter': False, 'department': True}

    def get_context_data(self, **kwargs):
        context = super(SDSDepartmentList, self).get_context_data(**kwargs)
        department = context["department"]
        sds = []
        for chemical in department.chemical_set.filter(archive=False):
            for sheet in chemical.safetydatasheet_set.all():
                sds.append(sheet)
        table = tables.SDSTable(sds)
        RequestConfig(
            self.request, paginate={'per_page': '25'}).configure(table)
        context['table'] = table
        context['tableheading'] = _("Safety Data Sheets")
        context['show_filter'] = self.filters
        context['plants'] = sorted(
            get_list_or_404(models.Plant), key=lambda x: x.name)
        context['target_name'] = "department_detail"
        return context


class ApprovalDocumentList(TableListView):
    """Returns a list of approval document."""
    model = models.Document
    table_class = tables.ApprovalTable
    table_heading = _("Approval Documents")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Document,
            doctype="FREIGABE",
            chemical__name__istartswith=letter,
        )


###############################################################################
# Stock Views
###############################################################################
class StockList(TableListView):
    """Returns the list of departments."""
    model = models.Stock
    table_class = tables.DepartmentStockTable
    table_heading = _("Departments")
    filters = {'letter': False, 'department': True}
    target_name = "stock_department_list"

    def get_table_data(self):
        return []


class StockDepartmentList(TableListMixin, DetailView):
    """Returns a list of stocks belonging to a departments."""
    model = models.Department
    table_class = tables.DepartmentStockTable
    table_heading = _("Stocks")
    filters = {'letter': False, 'department': True}
    target_name = "stock_department_list"

    def get_table_data(self):
        stocks = []
        for location in self.get_object().location_set.all():
            stocks.extend(location.stock_set.all())
        return stocks

    def get_context_data(self, **kwargs):
        context = super(StockDepartmentList, self).get_context_data(**kwargs)
        department = context["department"]
        context['tableheading'] = department.name
        return context


class LocationList(TableListView):
    """Returns a list of chemicals for a location."""
    model = models.Location
    table_heading = _("Stock Locations")
    table_class = tables.StockLocationTable
    template_name = 'chemicals/table_list.html'
    filters = {'location': True, }

    def get_table_data(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(LocationList, self).get_context_data(**kwargs)
        context['current_location'] = _(
            "Please choose a location from the list.")
        context['locations'] = self.get_location_list()
        return context


class ChemicalDepartment(DetailView):
    """Returns details about a stock."""
    model = models.Chemical
    template_name = "chemicals/chemical_department.html"

    def get_context_data(self, **kwargs):
        context = super(ChemicalDepartment, self).get_context_data(**kwargs)
        department = models.Department.objects.get(pk=self.kwargs["dep_id"])
        context["department"] = department
        context["stocks"] = context["chemical"].stock_set.filter(
            location__department=department)
        return context
