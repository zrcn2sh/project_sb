from django import forms
from .models import ProductList, ReqQuotation, CoEmp, OfferPrice, OfferPriceDetail, RentalList
from django.forms import inlineformset_factory

class DateInput(forms.DateInput):
    input_type = 'date'

class SelectInput(forms.Select):
    input_type = 'select'

class TextInput(forms.TextInput):
    input_type = 'text'

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['id','ProdDiv','ProdName','ProdBrand','VendorCode','Mercury_YN','AXProdCode','AXProdName','AXRegDate',
                  'ProdStatus','Basic_coprice','Basic_price','Inventory_YN','DTType','NTType','MTType','ETCType',
                  'DTCPU','DTCPUDetail','DTRAM','DTHDD','DTSSD','DTGraphicCard','DTPower','Keyboard_YN','DTMouse_YN',
                  'NTCPU','NTCPUDetail','NTRAM','NTHDD','NTSSD','NTPouch_YN','NTBag_YN','DTIORemark','NTGraphicCard',
                  'NTIORemark','MTIORemark','NTScreenSize','DTRemark','NTRemark','MTRemark','SRRemark','NTMouse_YN',
                  'MTScreenSize','NTWeight','DTWeight','MTWeight','SRWeight','Ratio','Resolution','Panel','ReqSpeed','BWRatio',
                  'SRInputWidth','SRCuttingSize','SRCapacity','SRPowerCon','ETCRemark1','ETCRemark2',
                  'ETCRemark3','RegUser','UpdateUser','Remark']
        widgets = {
                    'ProdDiv' : SelectInput(attrs={'onchange':'toggle_div(this.value);'}),
                    'AXRegDate' : DateInput()
             }

class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferPrice
        fields = ['OfferNo','OriginOfferNO','ReqNo','OfferDate','OfferResult']
        widgets = {
                    'OfferNo': TextInput(attrs={'readonly': 'True'}),
                    'OfferDate' : DateInput(),
             }

class OfferDetailForm(forms.ModelForm):
    class Meta:
        model = OfferPriceDetail
        exclude = ()

        OfferPriceDetailFormSet = inlineformset_factory(OfferPrice, OfferPriceDetail, fields=('OfferNo',))

class OrderAddInfoForm(forms.ModelForm):
    class Meta:
        model = OfferPrice
        fields = ['OfferNo','ClosingDate','PONumber','SignNumber','PZNumber']

        widgets = {
            'OfferNo': TextInput(attrs={'readonly': 'True'}),
            'ClosingDate' : DateInput(),
        }

class OrderDetailAddInfoForm(forms.ModelForm):
    class Meta:
        model = OfferPriceDetail
        fields = ['OfferNo','DeliveryDate','LogiType','LogiCompany','LogiNo','SerialNumber']

        widgets = {
            'OfferNo': TextInput(attrs={'readonly': 'True'}),
            'DeliveryDate' : DateInput(),
        }

class RentalListForm(forms.ModelForm):
    class Meta:
        model = RentalList
        fields = ['RentalNo','RentalType','RentalStatus','DeptCode','EmpNo','Custname','RentalVendor','RentalStartDate','RentalPeriod',
                  'RentalProdCode','RentalQty','RentalCoPrice','RentalOfferPrice']
        widgets = {
            'ReqNo': TextInput(attrs={'readonly':'True'}),
            'RentalStartDate': DateInput(),'RentalEndDate': DateInput(),
        }

