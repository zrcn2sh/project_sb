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

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        widgets = {
                'password' : TextInput(attrs={'type':'password'})
        }

