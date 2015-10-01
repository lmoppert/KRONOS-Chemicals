# vim: set fileencoding=utf-8 :
"""Views for the chemicals portal."""

from django.shortcuts import _get_queryset, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from django.db.models.functions import Lower
from django.db.models import Count, Q
from django.contrib import messages
from django_tables2 import SingleTableMixin, RequestConfig
from django import forms
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

    def filter_queryset(self, qs, archive=False):
        if self.request.LANGUAGE_CODE == 'de':
            qs = qs.filter(
                Q(synonym__chemical__region_de=True) |
                Q(identifier__chemical__region_de=True)
            )
        elif self.request.LANGUAGE_CODE == 'nl':
            qs = qs.filter(
                Q(synonym__chemical__region_be=True) |
                Q(identifier__chemical__region_be=True)
            )
        return qs.filter(
            Q(synonym__chemical__archive=archive) |
            Q(identifier__chemical__archive=archive)
        )

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
                department__plant=plant.id).order_by('department__name', 'name')
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


class TableDetailView(TableListMixin, DetailView):
    """Generic View that adds the TableListMixin to the DetailView"""


###############################################################################
# Main Views
###############################################################################
class ChemicalList(TableListView):
    """Returns a list of all Chemicals that are not archived."""
    model = models.ChemicalName
    table_heading = _("Chemicals")
    table_class = tables.ChemicalTable
    archive = False

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        qs = models.ChemicalName.objects.filter(name__istartswith=letter)
        return self.filter_queryset(qs, self.archive)


class ChemicalDetail(DetailView):
    """Returns details about a specific chemical."""
    model = models.Chemical

    def get_table_data(self):
        return self.get_object().consumer_set.all()

    def get_context_data(self, **kwargs):
        context = super(ChemicalDetail, self).get_context_data(**kwargs)
        context['table'] = tables.ConsumerStockTable(self.get_table_data())
        return context


class SDSList(TableListView):
    """Returns a list of safety data sheets."""
    model = models.SafetyDataSheet
    table_class = tables.SDSTable
    table_heading = _("Safety Data Sheets")
    target_name = "sds_department_list"
    filters = {'letter': False, 'department': True, 'items': True}

    def get_table_data(self):
        return []


class SDSDepartmentList(TableDetailView):
    """Returns a list of safety data sheets belonging to a department."""
    model = models.Department
    table_class = tables.SDSTable
    table_heading = _("Safety Data Sheets")
    target_name = "sds_department_list"
    filters = {'letter': False, 'department': True, 'items': True}

    def get_table_data(self):
        data = []
        department_id = self.get_object().id
        chemicals = models.ChemicalName.objects.filter(
            Q(synonym__chemical__departments__id=department_id) |
            Q(identifier__chemical__departments__id=department_id)
        ).annotate(name_lower=Lower('name'))
        for chemical in self.filter_queryset(chemicals).distinct():
            consumers = chemical.chemical.consumer_set.filter(
                department=department_id)
            for consumer in consumers:
                supplier = consumer.supplier
                data.append({'supplier': supplier, 'chemical': chemical})
        return data

    def get_context_data(self, **kwargs):
        context = super(SDSDepartmentList, self).get_context_data(**kwargs)
        department = context["department"]
        context['tablesubheading'] = department.name
        return context


class StockList(TableListView):
    """Returns the list of departments."""
    model = models.Stock
    table_class = tables.DepartmentConsumerTable
    table_heading = _("Departments (Stock View)")
    filters = {'letter': False, 'department': True}
    target_name = "stock_department_list"

    def get_table_data(self):
        return []


class StockDepartmentList(TableDetailView):
    """Returns a list of stocks belonging to a departments."""
    model = models.Department
    table_class = tables.DepartmentConsumerTable
    table_heading = _("Stocks")
    target_name = "stock_department_list"
    filters = {'letter': False, 'department': True, 'items': True}

    def get_table_data(self):
        department_id = self.get_object().id
        qs = models.ChemicalName.objects.filter(
            Q(synonym__chemical__departments__id=department_id) |
            Q(identifier__chemical__departments__id=department_id)
        ).extra(select={'department': department_id})
        return self.filter_queryset(qs)

    def get_context_data(self, **kwargs):
        context = super(StockDepartmentList, self).get_context_data(**kwargs)
        department = context["department"]
        context['tableheading'] = department.name
        return context


###############################################################################
# Chemical Views
###############################################################################
class ConsumerList(TableListView):
    """Returns a list of all Suppliers / Consumers."""
    model = models.Consumer
    table_class = tables.ConsumerTable
    table_heading = _("Suppliers")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(models.Consumer,
                                     supplier__name__istartswith=letter)


class CMRList(ConsumerList):
    """Returns a list of Suppliers for CMR Chemicals."""
    table_class = tables.CMRTable
    table_heading = _("Suppliers (CMR)")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        chemicals = []
        for h in models.HPhrase.objects.all():
            if h.cmr < 9:
                chemicals.extend(h.chemical_set.filter(archive=False).filter(
                    name__name__istartswith=letter)
                )
        return chemicals


class SupplierDetail(DetailView):
    """Returns details about a specific supplier."""
    model = models.Supplier


class DepartmentList(TableListView):
    """Returns the list of departments."""
    model = models.Department
    table_class = tables.DepartmentChemicalTable
    table_heading = _("Departments (Chemical View)")
    filters = {'letter': False, 'department': True}

    def get_table_data(self):
        return []


class DepartmentView(TableDetailView):
    """Returns the list of chemicals used in a specific department."""
    model = models.Department
    table_class = tables.DepartmentChemicalTable
    table_heading = _("Departments")
    filters = {'letter': True, 'department': True}

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        chemicals = []
        consumers = self.get_object().consumer_set.filter(
            chemical__name__name__istartswith=letter, chemical__archive=False)
        for consumer in consumers:
            chemicals.append(consumer.chemical)
        return chemicals

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        department = context["department"]
        context['tableheading'] = department.name
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
            doctype="f",
            chemical__name__name__istartswith=letter,
        )


###############################################################################
# SHE Views
###############################################################################
class ChemicalsMissingSDB(ChemicalList):
    """Returns a list of all Chemicals that do not have a SDS."""
    table_heading = _("Chemicals without SDS")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        chemicals = models.Chemical.objects.annotate(
            num_sds=Count('safetydatasheet')).filter(num_sds=0).filter(
            name__name__istartswith=letter).filter(archive=self.archive)
        chemical_names = []
        for chemical in chemicals:
            chemical_names.append(chemical.name)
        return chemical_names


class ToxList(TableListView):
    """Returns a list of Chemicals with Toxdata and SDS."""

    model = models.Toxdata
    table_class = tables.ToxTable


class ChemicalNumbers(ChemicalList):
    """Returns a list of all Chemicals that do not have a SDS."""
    table_class = tables.ChemicalNumberTable
    table_heading = _("Chemical Numbers")

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Chemical,
            name__name__istartswith=letter,
            archive=self.archive,
        )


###############################################################################
# Stock Views
###############################################################################
class LocationList(TableListView):
    """Returns the empty list for a location."""
    model = models.Location
    table_heading = _("Stock Locations")
    table_class = tables.StockLocationTable
    template_name = 'chemicals/table_list.html'
    filters = {'location': True, }

    def get_table_data(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(LocationList, self).get_context_data(**kwargs)
        context['locations'] = self.get_location_list()
        return context


class LocationView(TableDetailView):
    """Returns a list of chemicals for a location."""
    model = models.Location
    table_heading = _("Stock Locations")
    table_class = tables.StockLocationTable
    template_name = 'chemicals/table_list.html'
    filters = {'location': True, }

    def get_table_data(self):
        return self.get_object().stock_set.all()

    def get_table_heading(self):
        location = self.get_object()
        return u"{} - {} - {}".format(
            location.department.plant.name, location.department.name,
            location.name)

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['locations'] = self.get_location_list()
        return context


class ConsumerDetail(FormMixin, DetailView):
    """Returns details about a stock."""
    model = models.Consumer
    template_name = "chemicals/consumer_detail.html"
    formset_class = forms.inlineformset_factory(models.Chemical, models.Stock,
                                                extra=0, fields='__all__')

    def get_consumers(self):
        return models.Consumer.objects.filter(
            chemical=self.kwargs["chem_id"], department=self.kwargs["dep_id"])

    def get_sds(self, chemical):
        suppliers = []
        for consumer in self.get_consumers():
            suppliers.append(consumer.supplier)
        sds = chemical.safetydatasheet_set.filter(supplier_id__in=suppliers)
        esds = chemical.extendedsafetydatasheet_set.filter(
            supplier_id__in=suppliers)
        return sds, esds

    def get_object(self):
        return self.get_consumers().first()

    def get_department(self):
        return models.Department.objects.get(pk=self.kwargs["dep_id"])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        department = self.object.department
        chemical = self.object.chemical
        stocks = self.object.stocks
        sds, esds = self.get_sds(chemical)
        formset = self.formset_class(instance=chemical, queryset=stocks)
        context = self.get_context_data(formset=formset, department=department,
                                        stocks=stocks, chemical=chemical,
                                        sds=sds, esds=esds)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        department = self.object.department
        chemical = self.object.chemical
        sds, esds = self.get_sds(chemical)
        success_url = reverse('chemical_department', kwargs={
            'chem_id': chemical.id, 'dep_id': department.id, })
        formset = self.formset_class(instance=chemical,
                                     **self.get_form_kwargs())
        context = self.get_context_data(formset=formset, department=department,
                                        chemical=chemical, sds=sds, esds=esds)
        if formset.is_valid():
            formset.save()
            messages.success(request, _("Changes have been saved."))
            return HttpResponseRedirect(success_url)
        else:
            messages.error(request, _("Changes have not been saved yet. "
                                      "Errors are displayed below."))
            return self.render_to_response(context)


class ChemicalStockList(TableListView):
    """Returns the list of stocks for a chemical."""
    model = models.Chemical
    table_heading = _("Chemicals")
    table_class = tables.ChemicalStockTable
    filters = {'letter': True, 'department': False}
    target_name = "stock_department_list"
    archive = False

    def get_table_data(self):
        letter = self.get_filter_values()["letter"]
        return self.get_data_or_dict(
            models.Chemical,
            name__name__istartswith=letter,
            archive=self.archive,
        )

    def get_context_data(self, **kwargs):
        context = super(ChemicalStockList, self).get_context_data(**kwargs)
        table = tables.ChemicalStockTable(self.get_table_data())
        RequestConfig(
            self.request, paginate={'per_page': '25'}).configure(table)
        context['table'] = table
        return context
