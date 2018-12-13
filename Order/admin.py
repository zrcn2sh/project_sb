from django.contrib import admin

# Register your models here.

from Order.models import OfferPriceDetail, OfferPrice, RentalList

admin.site.register(OfferPriceDetail)
admin.site.register(OfferPrice)
admin.site.register(RentalList)