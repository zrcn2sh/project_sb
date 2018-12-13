from django.contrib import admin

# Register your models here.

from Prod.models import ReqQuotation, ProductList, ProductInventory
#from Prod.models import ProductList, ProductDetail_DT, ProductDetail_ETC, ProductDetail_MT, ProductDetail_NT, ProductDetail_SR, ProductInventory

admin.site.register(ReqQuotation)
admin.site.register(ProductList)
admin.site.register(ProductInventory)
