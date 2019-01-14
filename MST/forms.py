from django import forms
from .models import CoEmp, CoDept, CoUser, CoVendor
from django.contrib.auth.models import User

class TextInput(forms.TextInput):
    input_type = 'text'

class DateInput(forms.DateInput):
    input_type = 'date'



class VendorForm(forms.ModelForm):
    class Meta:
        model = CoVendor
        fields = ['id','CompanyName','Chief','Address','ComNumber','ComTel','Brand','Major_YN',
                  'ContactName1','ContactTel1','ContactCTel1','ContactMail1',
                  'ContactName2','ContactTel2','ContactCTel2','ContactMail2',
                  'AccountNo','Status','PaymentMethod','PaymentPeriod','Contract_YN',
                  'ContractDate','Remark','ComPaper','AccountPaper','RegUser','UpdateUser']
        widgets = {
                   'ContractDate' : DateInput()
                   }
    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['ComPaper'].required = False
        self.fields['AccountPaper'].required = False

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        widgets = {
                'password' : TextInput(attrs={'type':'password'})
        }

