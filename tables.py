"""Table definitions for the chemicals app."""

from operator import attrgetter
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import escape
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from .models import Chemical, Document, Supplier, Location, Stock


def render_as_list(objs):
    out = ""
    for obj in sorted(objs, key=attrgetter('name')):
        out += u'<span style="white-space: nowrap">{}</span><hr>'.format(
            escape(obj.name))
    return mark_safe(out[:-4])


def render_file_button(url, ext):
    button = """<a type="button" class="btn btn-warning btn-sm" href="{}"
    target="_blank"><span class="glyphicon glyphicon-file"></span> {}</a>"""
    return mark_safe(button.format(url, ext.upper()))


class RiskColumn(tables.Column):
    empty_values = ()

    def render(self, record):
        return render_as_list(record.risks.all())


class PictoColumn(tables.Column):
    empty_values = ()

    def render(self, record):
        return render_as_list(record.pictograms.all())


class SubstanceTable(tables.Table):
    """Table for the Substance View."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    wgk = tables.Column(
        empty_values=(),
        verbose_name=_('WGK'),
        orderable=False,
    )
    # Translators: This is an abbreviation for Storage Classes
    storage_classes = tables.Column(
        empty_values=(),
        verbose_name=_("SC"),
        orderable=False,
    )
    supplier_set = tables.Column(
        empty_values=(),
        verbose_name=_("Supplier"),
        orderable=False,
    )
    risks = RiskColumn(
        verbose_name=_("Risk Indication"),
        orderable=False,
    )
    pictograms = PictoColumn(
        verbose_name=_("Pictogram"),
        orderable=False,
    )

    def render_signal(self, record):
        s = record.signal
        if s == 'w' or s == u'w':
            r = u'<span class="label label-warning">%s</span>' % _("Warning")
        elif s == 'd' or s == u'd':
            r = u'<span class="label label-danger">%s</span>' % _("Danger")
        else:
            r = u'<span class="label label-default">%s</span>' % _("No Signal")
        return mark_safe(r)

    def render_storage_classes(self, record):
        return render_as_list(record.storage_classes.all())

    def render_wgk(self, record):
        return render_as_list(record.wgk.all())

    def render_supplier_set(self, record):
        contacts = []
        for supplier in record.supplier_set.all():
            contacts.append(supplier.contact)
        return render_as_list(set(contacts))

    class Meta:
        model = Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'risks', 'pictograms', 'signal', 'storage_classes',
                  'wgk', 'supplier_set', )


class DepartmentSubstanceTable(tables.Table):
    """Table for use in Department View"""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    risks = RiskColumn(verbose_name=_("Risk Indication"))
    pictograms = PictoColumn(verbose_name=_("Pictogram"))

    class Meta:
        model = Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('name', 'risks', 'pictograms')


class CMRSubstanceTable(tables.Table):
    """Table for use in Department View"""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    supplier_set = tables.Column(empty_values=(), verbose_name=_("Supplier"))

    def render_supplier_set(self, record):
        contacts = []
        for supplier in record.supplier_set.all():
            contacts.append(supplier.contact)
        return render_as_list(set(contacts))

    class Meta:
        model = Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('name', 'supplier_set')


class CMRTable(tables.Table):
    """Table listing all CMR chemicals."""
    contact = tables.LinkColumn('contact_detail',
                                accessor='contact.name',
                                args=[A('contact.pk')],
                                verbose_name=_('Supplier'))
    chemical = tables.LinkColumn('chemical_detail',
                                 accessor='chemical.name',
                                 args=[A('chemical.pk')],
                                 verbose_name=_('Chemical'))
    department = tables.Column(accessor='department.name',
                               verbose_name=_('Department'))

    class Meta:
        model = Supplier
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('contact', 'chemical')
        fields = ('chemical', 'department', 'contact',)
        # fields = ('chemical', 'CMR category', 'department', 'contact',)


class SupplierTable(tables.Table):
    """Table listing all suppliers."""
    contact = tables.LinkColumn('contact_detail',
                                accessor='contact.name',
                                args=[A('contact.pk')],
                                verbose_name=_('Supplier'))
    chemical = tables.LinkColumn('chemical_detail',
                                 accessor='chemical.name',
                                 args=[A('chemical.pk')],
                                 verbose_name=_('Chemical'))
    department = tables.Column(accessor='department.name',
                               verbose_name=_('Department'))

    class Meta:
        model = Supplier
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('contact', 'chemical')
        fields = ('contact', 'chemical', 'department',)


class SDSTable(tables.Table):
    """Table listing safety data sheets."""
    sds = tables.Column(accessor="file", verbose_name=_("SDS"))
    esds = tables.FileColumn(accessor="file", verbose_name=_("eSDS"))
    language = tables.Column(accessor="country_code",
                             verbose_name=_("Language"))
    chemical = tables.LinkColumn('chemical_detail', args=[A('chemical.pk')],
                                 accessor='chemical.name',
                                 verbose_name=_("Chemical"))
    departments = tables.Column(accessor='supplier',
                                verbose_name=_("Departments"))
    risks = RiskColumn(accessor='chemical.risks', verbose_name=_("Risks"))
    pictograms = PictoColumn(accessor='chemical.pictograms',
                             verbose_name=_("Pictograms"))
    supplier = tables.Column(accessor='supplier.name',
                             verbose_name=_("Supplier"))

    def render_sds(self, record):
        return render_file_button(record.file.url, record.file.extension)

    def render_esds(self, record):
        try:
            esds = record.chemical.extendedsafetydatasheet_set.get(
                supplier=record.supplier)
        except:
            return ''
        return render_file_button(esds.file.url, esds.file.extension)

    def render_departments(self, record):
        department_list = []
        suppliers = record.supplier.supplier_set.filter(
            chemical_id=record.chemical_id)
        for supplier in suppliers:
            department_list.append(supplier.department)
        return render_as_list(department_list)

    def render_risks(self, record):
        return render_as_list(record.chemical.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.chemical.pictograms.all())

    class Meta:
        attrs = {'class': "table table-bordered table-striped table-condensed"}


class ApprovalTable(tables.Table):
    """Table listing approval documents."""
    document = tables.Column(accessor="file", verbose_name=_("Approval"))
    chemical = tables.LinkColumn('chemical_detail', args=[A('chemical.pk')],
                                 accessor='chemical.name',
                                 verbose_name=_("Chemical"))

    def render_document(self, record):
        return render_file_button(record.file.url, record.file.extension)

    class Meta:
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        model = Document
        order_by = ('name',)
        fields = ('document', 'chemical', 'plant')


class DepartmentTable(tables.Table):
    """Table displaying a Department."""

    class Meta:
        model = Location
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('department', 'chemical', 'risks', 'pictograms', 'stock',
                  'max_volume', 'max_unit')


class DepartmentStockTable(tables.Table):
    """Table displaying Stocks of a Department."""
    # department = tables.Column(
    #     accessor='location.department.name', verbose_name=_("Department"))
    chemical = tables.LinkColumn(
        'chemical_department',
        args=[A('chemical.pk'), A('location.department.pk')],
        verbose_name=_("Chemical"))
    risks = RiskColumn(
        accessor='chemical.risks', verbose_name=_("Risks"))
    pictograms = PictoColumn(
        accessor='chemical.pictograms', verbose_name=_("Pictograms"))
    location = tables.Column(
        accessor='location.name', verbose_name=_("Location"))

    def render_risks(self, record):
        return render_as_list(record.chemical.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.chemical.pictograms.all())

    class Meta:
        model = Stock
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('location.name',)
        fields = ('chemical', 'risks', 'pictograms',
                  'location', 'max_volume', 'max_unit')
