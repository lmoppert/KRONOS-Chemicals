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
        return render_as_list(record.chemical.risks.all())


class PictoColumn(tables.Column):
    empty_values = ()

    def render(self, record):
        return render_as_list(record.chemical.pictograms.all())


class ChemicalNumberTable(tables.Table):
    """Table for the Chemical View."""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')])

    class Meta:
        model = models.Chemical
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        fields = ('name', 'preparation', 'article', 'cas', 'einecs', )


class ChemicalTable(tables.Table):
    """Table for the Chemical View."""
    name = tables.LinkColumn(
        'chemical_detail',
        accessor='name',
    )
    wgk = tables.Column(
        verbose_name=_('WGK'),
        accessor='chemical.wgk.name',
        orderable=False,
    )
    # Translators: This is an abbreviation for Storage Classes
    storage_class = tables.Column(
        verbose_name=_("SC"),
        accessor='chemical.storage_class.name',
        orderable=False,
    )
    signal = tables.Column(
        empty_values=(),
        verbose_name=_("Signal"),
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

    def render_name(self, record):
        name = record.name
        url = reverse('chemical_detail', kwargs={'pk': record.chemical.id})
        if record.polymorphic_ctype.model == u'synonym':
            r = u'<a href="{}"><em>{}</em></a>'.format(url, name)
        else:
            r = u'<a href="{}">{}</a>'.format(url, name)
        return mark_safe(r)

    def render_signal(self, record):
        s = record.chemical.signal
        if s == 'w' or s == u'w':
            r = u'<span class="label label-warning">%s</span>' % _("Warning")
        elif s == 'd' or s == u'd':
            r = u'<span class="label label-danger">%s</span>' % _("Danger")
        elif s == 'n' or s == u'n':
            r = u'<span class="label label-default">%s</span>' % _("No Signal")
        else:
            r = u''
        return mark_safe(r)

    def render_supplier_set(self, record):
        suppliers = []
        for consumer in record.chemical.consumer_set.all():
            suppliers.append(consumer.supplier)
        return render_as_list(set(suppliers))

    class Meta:
        model = models.Identifier
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('name',)
        fields = ('name', 'risks', 'pictograms', 'signal', 'storage_class',
                  'wgk', 'supplier_set', )


class DepartmentChemicalTable(tables.Table):
    """Table for use in Department View"""
    name = tables.LinkColumn('chemical_detail', args=[A('pk')],
                             accessor='name.name',)
    risks = tables.Column(
        verbose_name=_("Risk Indication"),
        orderable=False,
        empty_values=(),
    )
    pictograms = PictoColumn(
        verbose_name=_("Pictogram"),
        orderable=False,
        empty_values=(),
    )

    def render_risks(self, record):
        return render_as_list(record.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.pictograms.all())

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
        suppliers = []
        for consumer in record.consumer_set.all():
            suppliers.append(consumer.supplier)
        return render_as_list(set(suppliers))

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
        suppliers = []
        for consumer in record.consumer_set.all():
            suppliers.append(consumer.supplier)
        return render_as_list(set(suppliers))

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
                                 accessor='chemical.name.name',
                                 args=[A('chemical.pk')],
                                 verbose_name=_('Chemical'))
    department = tables.Column(accessor='department.name',
                               verbose_name=_('Department'))

    class Meta:
        model = models.Consumer
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('supplier', 'chemical')
        fields = ('supplier', 'chemical', 'department', 'comment')


class ConsumerStockTable(tables.Table):
    """Table listing the consumers for one chemical and related stocks"""
    department = tables.LinkColumn('chemical_department',
                                   accessor="department.name",
                                   args=[A('chemical.pk'), A('department.pk')],
                                   verbose_name=_("Department"))
    supplier = tables.LinkColumn('supplier_detail',
                                 accessor='supplier.name',
                                 args=[A('supplier.pk')],
                                 verbose_name=_('Supplier'))
    stocks = tables.Column(empty_values=(), accessor='stocks',
                           verbose_name=_("Chemical Stocks"), orderable=False,)

    def render_stocks(self, record):
        stocks = u'<table class="table table-bordered table-condensed">\n'
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

    class Meta:
        model = models.Consumer
        attrs = {'class': "table table-bordered table-striped table-condensed"}
        order_by = ('department', 'supplier')
        fields = ('department', 'supplier', 'stocks')


class SDSTable(tables.Table):
    """Table listing safety data sheets."""
    sds = tables.Column(
        empty_values=(),
        orderable=False,
        verbose_name=_("SDS"),
    )
    esds = tables.FileColumn(
        empty_values=(),
        orderable=False,
        verbose_name=_("eSDS"),
    )
    chemical = tables.LinkColumn(
        'chemical_detail',
        verbose_name=_("Chemical"),
        accessor='chemical.name',
        order_by=('chemical.name_lower'),
    )
    risks = RiskColumn(
        verbose_name=_("Risks"),
        orderable=False,
    )
    pictograms = PictoColumn(
        verbose_name=_("Pictograms"),
        orderable=False,
    )
    supplier = tables.Column(
        verbose_name=_("Supplier"),
        orderable=False,
    )

    def render_chemical(self, record):
        name = record['chemical']
        url = reverse('chemical_detail', kwargs={'pk': name.chemical.id})
        if name.polymorphic_ctype.model == u'synonym':
            r = u'<a href="{}"><em>{}</em></a>'.format(url, name.name)
        else:
            r = u'<a href="{}">{}</a>'.format(url, name.name)
        return mark_safe(r)

    def render_sds(self, record):
        chemical = record['chemical'].chemical
        supplier = record['supplier']
        r = u'<ul class="list-unstyled">'
        for sds in chemical.safetydatasheet_set.filter(supplier=supplier):
            r += '<li style="margin-bottom:10px">{}</li>'.format(
                render_file_button(sds.file.url, sds.country_code.upper()))
        r += u'</ul>'
        return mark_safe(r)

    def render_esds(self, record):
        chemical = record['chemical'].chemical
        supplier = record['supplier']
        r = u'<ul class="list-unstyled">'
        for sds in chemical.extendedsafetydatasheet_set.filter(
                supplier=supplier):
            r += '<li style="margin-bottom:10px">{}</li>'.format(
                render_file_button(sds.file.url, sds.country_code.upper()))
        r += u'</ul>'
        return mark_safe(r)

    def render_risks(self, record):
        chemical = record['chemical'].chemical
        return render_as_list(chemical.risks.all())

    def render_pictograms(self, record):
        chemical = record['chemical'].chemical
        return render_as_list(chemical.pictograms.all())

    class Meta:
        attrs = {'class': "table table-bordered table-striped table-condensed"}


class ApprovalTable(tables.Table):
    """Table listing approval documents."""
    document = tables.Column(accessor="file", verbose_name=_("Approval"))
    chemical = tables.LinkColumn('chemical_detail', args=[A('chemical.pk')],
                                 accessor='chemical.name.name',
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
        accessor='name',
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
        verbose_name=_("Chemical Stocks"),
        orderable=False,
    )

    def render_chemical(self, record):
        name = record.name
        url = reverse('chemical_department', kwargs={
            'chem_id': record.chemical.id,
            'dep_id': record.department
        })
        if record.polymorphic_ctype.model == u'synonym':
            r = u'<a href="{}"><em>{}</em></a>'.format(url, name)
        else:
            r = u'<a href="{}">{}</a>'.format(url, name)
        return mark_safe(r)

    def render_stocks(self, record):
        stocks = u'<table class="{}">\n'.format(self.Meta.attrs['class'])
        for stock in record.chemical.stock_set.filter(
                location__department=record.department):
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
    risks = tables.Column(
        empty_values=(),
        verbose_name=_("Risk Indication"),
        orderable=False,
    )
    pictograms = tables.Column(
        empty_values=(),
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

    def render_risks(self, record):
        return render_as_list(record.risks.all())

    def render_pictograms(self, record):
        return render_as_list(record.pictograms.all())

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
        'chemical_detail', accessor='chemical.name.name',
        args=[A('chemical.pk')])
    supplier = tables.Column(accessor='supplier.name')
    sds = tables.Column(accessor='chemical.safetydatasheet.first')
