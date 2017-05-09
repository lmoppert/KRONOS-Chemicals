"""URL config for the chemical protal."""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.conf.urls import url
from .views import (ChemicalList, ChemicalDetail, ConsumerDetail,
                    ConsumerList, CMRList, StockList, SupplierDetail,
                    DepartmentList, DepartmentView, SDSList, SDSDepartmentList,
                    ApprovalDocumentList, LocationList, LocationView,
                    StockDepartmentList, ChemicalStockList, ChemicalsMissingSDB,
                    ChemicalNumbers)


urlpatterns = [
    #########################
    # Chemical Views
    url(r'^(?P<pk>\d+)$', ChemicalDetail.as_view(), name='chemical_detail'),
    url(r'^chemicals/$', ChemicalList.as_view(), name='chemical_list'),
    url(r'^archived/$', ChemicalList.as_view(archive=True, table_heading=_(
        'Archived chemicals')), name='archived_chemicals'),
    url(r'^supplier/(?P<pk>\d+)$', SupplierDetail.as_view(),
        name='supplier_detail'),
    url(r'^department/(?P<pk>\d+)$', DepartmentView.as_view(),
        name='department_detail'),
    url(r'^departments/$', DepartmentList.as_view(), name='department_list'),
    url(r'^suppliers/$', ConsumerList.as_view(), name='supplier_list'),
    url(r'^cmr/$', CMRList.as_view(), name='cmr_list'),
    url(r'^sds/department/(?P<pk>\d+)$', SDSDepartmentList.as_view(),
        name='sds_department_list'),
    url(r'^sds/$', SDSList.as_view(), name='sds_list'),
    url(r'^approval/$', ApprovalDocumentList.as_view(), name='approval_list'),
    #########################
    # SHE Views
    url(r'^missingsdb/$', ChemicalsMissingSDB.as_view(),
        name='chemical_missing_sdb'),
    url(r'numbers/$', ChemicalNumbers.as_view(), name='chemical_numbers'),
    #########################
    # Stock Views
    url(r'^stocks/department/(?P<pk>\d+)$', StockDepartmentList.as_view(),
        name='stock_department_list'),
    url(r'^stocks/$', StockList.as_view(), name='stock_list'),
    url(r'^chemical/(?P<chem_id>\d+)/department/(?P<dep_id>\d+)$',
        ConsumerDetail.as_view(), name='chemical_department'),
    url(r'^locations/$', LocationList.as_view(), name='location_list'),
    url(r'^location/(?P<pk>\d+)$', LocationView.as_view(),
        name='stock_location_list'),
    url(r'^chemicalstocks/$', ChemicalStockList.as_view(),
        name='chemical_stock_list'),
    #########################
    # Generic Views
    url(r'^$', RedirectView.as_view(url=reverse_lazy('chemical_list'),
                                    permanent=True), name='home'),
]
