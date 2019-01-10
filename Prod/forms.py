from django import forms
from .models import ProductList, ReqQuotation, CoEmp

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
                  'ETCRemark3','RegUser','UpdateUser','Remark','DTOS','NTOS','Warranty']
        widgets = {
                    'ProdDiv' : SelectInput(attrs={'onchange':'toggle_div(this.value);'}),
                    'AXRegDate' : DateInput()
             }

class ReqQuotaionForm(forms.ModelForm):
    class Meta:
        model = ReqQuotation
        fields = ['ReqNo','OriginReqNo','DeptCode','EmpNo','Custname','RPCustname','Rental_YN','Bid_YN','ReqProd',
                  'Remark','CanonETC','ShipDT','ReqDate','Status','ReqVendor1','ReqVendor2','ReqVendor3',
                  'VendorReqUser','FailReason','RegUser','UpdateUser','StatusA_Date','StatusR_Date',
                  'StatusS_Date','StatusO_Date','StatusC_Date','StatusF_Date']
        widgets = {
            'ReqNo': TextInput(attrs={'readonly':'True'}),
            'StatusA_Date': DateInput(),'StatusR_Date': DateInput(),
            'StatusS_Date': DateInput(),'StatusO_Date': DateInput(),
            'StatusC_Date': DateInput(),'StatusF_Date': DateInput(),
            'ShipDT': DateInput()
        }

