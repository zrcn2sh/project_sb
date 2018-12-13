"""project_sb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #인증 관련
from MST import views as viewsMST
from Prod import views as viewsProd
from Order import views as viewsOrder

urlpatterns = (
    url(r'^$', viewsMST.signin, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls', namespace="books")),

    url(r'^MST/vendor/', viewsMST.Vendor, name='Vendor'),
    url(r'^MST/vendornew/', viewsMST.VendorNew, name='VendorNew'),
    url(r'^MST/vendoredit/(?P<pk>\d+)', viewsMST.VendorEdit, name='VendorEdit'),
    url(r'^MST/dept/', viewsMST.Dept, name='Dept'),

    url(r'^Prod/quotation/', viewsProd.Quotation, name='Quotation'),
    url(r'^Prod/quotationnew/', viewsProd.ReqQuotationNew, name='QuotationNew'),
    url(r'^Prod/quotationedit/(?P<pk>\d+)', viewsProd.ReqQuotationEdit, name='QuotationEdit'),
    url(r'^Prod/quotationchange/(?P<pk>\d+)', viewsProd.ReqQuotationChange, name='QutationChange'),
    url(r'^Prod/sendmail/(?P<pk>\d+)', viewsProd.SendmailQuotation, name='SendmailQuotation'),
    url(r'^Prod/product/', viewsProd.ProductMaster, name='Product'),
    url(r'^Prod/productnew/', viewsProd.ProductNew, name='ProductNew'),
    url(r'^Prod/productedit/(?P<pk>\d+)', viewsProd.ProductEdit, name='ProductEdit'),
    url(r'^Prod/inventory/', viewsProd.Inventory, name='ProductInventory'),
    url(r'^Prod/search/(?P<offerpk>\d+)', viewsProd.SearchProductOffer, name='SearchProductOffer'),
    url(r'^Prod/SetQuotationPrice/(?P<prodpk>\d+)/(?P<offerpk>\d+)', viewsOrder.SetQuotationPrice, name='SetPriceProd'),

    url(r'^Order/offer/', viewsOrder.Offer, name='OfferPrice'),
    url(r'^Order/order/', viewsOrder.OrderList, name='OrderList'),
    url(r'^Order/offernew/(?P<pk>\d+)', viewsOrder.OfferNew, name='OfferPriceNew'),
    url(r'^Order/offeredit/(?P<pk>\d+)', viewsOrder.OfferEdit, name='OfferPriceEdit'),
    url(r'^Order/offerdetail/(?P<pk>\d+)', viewsOrder.OfferDetail, name='OfferPriceDetail'),
    url(r'^Order/offerprint/(?P<pk>\d+)', viewsOrder.OfferPrint, name='OfferPrint'),
    url(r'^Order/offerorder/(?P<pk>\d+)', viewsOrder.OfferOrder, name='OfferOrder'),
    url(r'^Order/confirm/(?P<pk>\d+)', viewsOrder.OrderConfirm, name='OrderConfirm'),
    url(r'^Order/orderaddinfo/(?P<pk>\d+)', viewsOrder.OrderAddInfo, name='OrderAddInfo'),
    url(r'^Order/orderdetailaddinfo/(?P<pk>\d+)', viewsOrder.OrderDetailAddInfo, name='OrderDetailAddInfo'),
    url(r'^Order/delofferdetail/(?P<pk>\d+)', viewsOrder.OfferDelete, name='OfferDelete'),
    url(r'^Order/rental/', viewsOrder.Rental, name='Rental'),
    url(r'^Order/rentalnew/', viewsOrder.RentalNew, name='RentalNew'),
    url(r'^Order/rentaledit/(?P<pk>\d+)', viewsOrder.RentalEdit, name='RentalEdit'),
    url(r'^login/', viewsMST.signin, name='login'),

)

"""urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"""
