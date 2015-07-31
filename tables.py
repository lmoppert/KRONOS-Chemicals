"""Table definitions for the chemicals app."""

from operator import attrgetter
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from . import models


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


class ChemicalNumberTable(tables.Table):
    """Table for the Chemical View."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'preparation', 'article', 'cas', 'einecs', )


class ChemicalTable(tables.Table):
    """Table for the Chemical View."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    wgk = tables.Column(verbose_name=_('WGK'), accessor='wgk.name')
    # Translators: This is an abbreviation for Storage Classes
    storage_class = tables.Column(verbose_name=_("SC"),
                                  accessor='storage_class.name')
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

    def render_supplier_set(self, record):
        consumers = []
        for consumer in record.consumer_set.all():
            consumers.append(consumer.supplier)
        return render_as_list(set(consumers))

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'risks', 'pictograms', 'signal', 'storage_class',
                  'wgk', 'supplier_set', )


class DepartmentChemicalTable(tables.Table):
    """Table for use in Department View"""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    risks = RiskColumn(verbose_name=_("Risk Indication"))
    pictograms = PictoColumn(verbose_name=_("Pictogram"))

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('name', 'risks', 'pictograms')


class CMRChemicalTable(tables.Table):
    """Table for use in Department View"""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    supplier_set = tables.Column(empty_values=(), verbose_name=_("Supplier"))

    def render_supplier_set(self, record):
        consumers = []
        for consumer in record.consumer_set.all():
            consumers.append(consumer.supplier)
        return render_as_list(set(consumers))

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('name', 'supplier_set')


class CMRTable(tables.Table):
    """Table listing all CMR chemicals."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    cmr = tables.Column(
        empty_values=(),
        verbose_name=_('CMR Category'),
        orderable=False,
    )
    supplier_set = tables.Column(
        empty_values=(),
        verbose_name=_("Supplier"),
        orderable=False,
    )

    def render_cmr(self, record):
        if record.cmr1:
            return "1A/1B"
        else:
            return "2"

    def render_supplier_set(self, record):
        consumers = []
        for consumer in record.consumer_set.all():
            consumers.append(consumer.supplier)
        return render_as_list(set(consumers))

    class Meta:
        model = models.Supplier
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'cmr', 'supplier_set')


class ConsumerTable(tables.Table):
    """Table listing all suppliers."""
    supplier = tables.LinkColumn('supplier_detail',
                                 accessor='supplier.name',
                                 args=[A('supplier.pk')],
                                 verbose_name=_('Supplier'))
    chemical = tables.LinkColumn('chemical_detail',
                                 accessor='chemical.name',
                                 args=[A('chemical.pk')],
                                 verbose_name=_('Chemical'))
    department = tables.Column(accessor='department.name',
                               verbose_name=_('Department'))

    class Meta:
        model = models.Consumer
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('supplier', 'chemical')
        fields = ('supplier', 'chemical', 'department', 'comment')


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
        model = models.Document
        order_by = ('name',)
        fields = ('document', 'chemical', 'plant')


class DepartmentTable(tables.Table):
    """Table displaying a Department."""

    class Meta:
        model = models.Location
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('department', 'chemical', 'risks', 'pictograms', 'stock',
                  'max_volume', 'max_unit')


class DepartmentConsumerTable(tables.Table):
    """Table displaying Stocks of a Department."""
    chemical = tables.LinkColumn(
        'chemical_department',
        args=[A('chemical.pk'), A('department.pk')],
        verbose_name=_("Chemical"),
    )
    risks = RiskColumn(
        accessor='chemical.risks',
        verbose_name=_("Risks"),
        orderable=False,
    )
    pictograms = PictoColumn(
        accessor='chemical.pictograms',
        verbose_name=_("Pictograms"),
        orderable=False,
    )
    stocks = tables.Column(
        empty_values=(),
        accessor='stocks',
        verbose_name=_("Chemical Stocks"),
        orderable=False,
    )

    def render_stocks(self, record):
        stocks = u'<table class="{}">\n'.format(self.Meta.attrs['class'])
        for stock in record.stocks.all():
            row = u'<tr><td class="location">{}</td>\n' \
                  '<td class="volume">{} {}</td></tr>\n'
            stocks += row.format(
                stock.location.name,
                stock.max_volume,
                models.Stock.UNITS[stock.max_unit],
            )
        stocks += '</table>'
        return mark_safe(stocks)

    def render_risks(self, record):
        return render_as_list(record.chemical.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.chemical.pictograms.all())

    class Meta:
        model = models.Consumer
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('chemical', 'risks', 'pictograms', 'stocks')


class ChemicalStockTable(tables.Table):
    """Table displaying Stocks that containing a dedicaded chemical."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])
    stock_set = tables.Column(
        empty_values=(),
        verbose_name=_("Chemical Stocks"),
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

    def render_stock_set(self, record):
        stocks = u'<table class="{}">\n'.format(self.Meta.attrs['class'])
        for stock in record.stock_set.all():
            url = reverse('chemical_department', kwargs={
                'chem_id': record.id, 'dep_id': stock.location.department.id, })
            row = u'<tr><td class="department"><a href="{}">{}</a></td>\n' \
                  '<td class="location">{}</td>\n' \
                  '<td class="volume">{} {}</td></tr>\n'
            stocks += row.format(
                url, stock.location.department.name, stock.location.name,
                stock.max_volume, models.Stock.UNITS[stock.max_unit],)
        stocks += '</table>'
        return mark_safe(stocks)

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'stock_set', 'risks', 'pictograms', )


class StockLocationTable(tables.Table):
    """Table for the Location List."""
    chemical = tables.LinkColumn(
        'chemical_department',
        args=[A('chemical.pk'), A('location.department.pk')],
        verbose_name=_("Chemical")
    )
    wgk = tables.Column(
        accessor='chemical.wgk.name',
        verbose_name=_('WGK')
    )
    # Translators: This is an abbreviation for Storage Classes
    storage_class = tables.Column(
        accessor='chemical.storage_class.name',
        verbose_name=_("SC")
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

    def render_risks(self, record):
        return render_as_list(record.chemical.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.chemical.pictograms.all())

    class Meta:
        model = models.Stock
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('location.name',)
        fields = ('chemical', 'storage_class', 'wgk', 'risks', 'pictograms', )


class ToxTable(tables.Table):
    """Table for the Toxdata of a Chemical."""
    # TODO: This has not been finished, the SDS should be displayed in a nested
    #       table instead of using it in the main table. The main reason for
    #       that is performance, but .select_related may also do the trick. Will
    #       test this on the Stock View for chemicals first!
    name = tables.LinkColumn(
        'chemical_detail', accessor='chemical.name', args=[A('chemical.pk')])
    supplier = tables.Column(accessor='supplier.name')
    sds = tables.Column(accessor='chemical.safetydatasheet.first')
