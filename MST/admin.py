from django.contrib import admin

# Register your models here.

from MST.models import CoDept, CoEmp, CoUser, CoVendor

admin.site.register(CoUser)
admin.site.register(CoEmp)
admin.site.register(CoDept)
admin.site.register(CoVendor)
