from django.contrib.auth.models import User
from django import forms
import django_filters
from .models import ProductList
from MST.models import CoVendor
from project_sb.global_variables import *

class OrderListFilter(django_filters.FilterSet):
    ProdName = django_filters.CharFilter(lookup_expr='icontains')
    ProdBrand = django_filters.CharFilter(lookup_expr='icontains')
    ProdDiv = django_filters.MultipleChoiceFilter(choices=Product_Div,widget=forms.CheckboxSelectMultiple)
    VendorCode = django_filters.ModelMultipleChoiceFilter(queryset=CoVendor.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)
    ProdStatus = django_filters.MultipleChoiceFilter(choices=Product_status,widget=forms.CheckboxSelectMultiple)
    #데스크탑
    DTType = django_filters.MultipleChoiceFilter(choices=DT_enumtype, widget=forms.CheckboxSelectMultiple)
    DTCPU = django_filters.MultipleChoiceFilter(choices=CPU_enumtype, widget=forms.CheckboxSelectMultiple)
    DTCPUDetail = django_filters.CharFilter(lookup_expr='icontains')
    DTRAM = django_filters.MultipleChoiceFilter(choices=RAM_enumtype, widget=forms.CheckboxSelectMultiple)
    DTHDD = django_filters.MultipleChoiceFilter(choices=HDD_enumtype, widget=forms.CheckboxSelectMultiple)
    DTSSD = django_filters.MultipleChoiceFilter(choices=SSD_enumtype, widget=forms.CheckboxSelectMultiple)
    DTGraphicCard = django_filters.CharFilter(lookup_expr='icontains')

    #모니터
    MTType = django_filters.MultipleChoiceFilter(choices=MT_enumtype, widget=forms.CheckboxSelectMultiple)
    Ratio= django_filters.MultipleChoiceFilter(choices=Ratio_enumtype, widget=forms.CheckboxSelectMultiple)
    Resolution = django_filters.MultipleChoiceFilter(choices=Resolution_enumtype, widget=forms.CheckboxSelectMultiple)
    Panel = django_filters.MultipleChoiceFilter(choices=Panel_enumtype, widget=forms.CheckboxSelectMultiple)

    #노트북
    NTType = django_filters.MultipleChoiceFilter(choices=DT_enumtype, widget=forms.CheckboxSelectMultiple)
    NTCPU = django_filters.MultipleChoiceFilter(choices=CPU_enumtype, widget=forms.CheckboxSelectMultiple)
    NTCPUDetail = django_filters.CharFilter(lookup_expr='icontains')
    NTRAM = django_filters.MultipleChoiceFilter(choices=RAM_enumtype, widget=forms.CheckboxSelectMultiple)
    NTHDD = django_filters.MultipleChoiceFilter(choices=HDD_enumtype, widget=forms.CheckboxSelectMultiple)
    NTSSD = django_filters.MultipleChoiceFilter(choices=SSD_enumtype, widget=forms.CheckboxSelectMultiple)
    NTGraphicCard = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ProductList
        fields = ['ProdName','ProdBrand','ProdDiv','VendorCode','ProdStatus',
                  'DTType','DTCPU','DTCPUDetail','DTRAM','DTHDD','DTSSD','DTGraphicCard',
                  'MTType','Ratio','Resolution','Panel',
                  'NTType','NTCPU','NTCPUDetail','NTRAM','NTHDD','NTSSD','NTGraphicCard',
                  'Basic_coprice','Basic_price']
