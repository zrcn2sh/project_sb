from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F, FloatField, IntegerField
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Order.models import OfferPrice, OfferPriceDetail, ReqQuotation, RentalList
from Prod.models import ProductList
from .forms import OfferForm, OfferDetailForm, OrderAddInfoForm, OrderDetailAddInfoForm, RentalListForm
from .render import Render
import datetime
from .filters import OrderListFilter


# Create your views here.
@login_required

def Offer(request):
    offerprice = OfferPrice.objects.prefetch_related('Offer_No').select_related('ReqNo').annotate(
        qtytotal=Sum('Offer_No__Qty'),
        copricetotal=Sum(F('Offer_No__CoPrice') * F('Offer_No__Qty')),
        offerpricetotal=Sum(F('Offer_No__OfferPrice') * F('Offer_No__Qty'))
    ).annotate(
        totalmargin =  100 - Cast(F('copricetotal'), FloatField()) / Cast(F('offerpricetotal'), FloatField()) * 100
    ).all()

    context = {'offerprice':offerprice}

    return render(request, 'Order/Offer.html', context)

@login_required
def OfferNew(request, pk):
    quotation = ReqQuotation.objects.filter(pk=pk).all()
    quostatus = quotation.values_list('Status', flat=True)

    if quostatus[0] == 'R':
        ReqQuotation.objects.filter(pk=pk).update(Status='S')
        ReqQuotation.objects.filter(pk=pk).update(StatusS_Date=datetime.datetime.now())

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            offer_id = str(form.instance.id)

        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.location.href="../offerdetail/'+offer_id+';"</script>')
    else:
        form = OfferForm(initial={'ReqNo':pk})

    return render(request, 'Order/new_Offer.html', {'form':form})

@login_required
def OfferEdit(request, pk):
    post = get_object_or_404(OfferPrice, pk=pk)
    if request.method == 'POST':
        form = OfferForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            offer_id = str(form.instance.id)

            return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.location.href="../offerdetail/' + offer_id + ';"</script>')
    else:
        form = OfferForm(instance=post)

    return render(request, 'Order/SetPriceProd.html', {'form':form})

@login_required
def OfferDetail(request, pk):
    offerprice = OfferPrice.objects.prefetch_related('Offer_No').select_related('ReqNo').annotate(
        qtytotal=Sum('Offer_No__Qty'),
        copricetotal=Sum(F('Offer_No__CoPrice') * F('Offer_No__Qty')),
        offerpricetotal=Sum(F('Offer_No__OfferPrice') * F('Offer_No__Qty'))
    ).annotate(
        totalmargin =  100 - Cast(F('copricetotal'), FloatField()) / Cast(F('offerpricetotal'), FloatField()) * 100
    ).filter(
        pk=pk
    ).all()

    context = {'offerprice':offerprice}

    return render(request, 'Order/offerdetail.html', context)

@login_required
def SetQuotationPrice(request, prodpk, offerpk):

    offerprice = OfferPrice.objects.prefetch_related('Offer_No').select_related('ReqNo').annotate(
        qtytotal=Sum('Offer_No__Qty'),
        copricetotal=Sum(F('Offer_No__CoPrice') * F('Offer_No__Qty')),
        offerpricetotal=Sum(F('Offer_No__OfferPrice') * F('Offer_No__Qty'))
    ).annotate(
        totalmargin=100 - Cast(F('copricetotal'), FloatField()) / Cast(F('offerpricetotal'), FloatField()) * 100
    ).filter(
        Offer_No__ProdCode=prodpk
    ).all()


    prodinfo = ProductList.objects.filter(pk=prodpk).all()

    if request.method == 'POST':
        form = OfferDetailForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(
                '<script type="text/javascript">alert("저장안되었습니다.");window.close()</script>')
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.opener.location.reload();</script>')
    else:
        form = OfferDetailForm(initial={'OfferNo':offerpk,'ProdCode':prodpk})

    context = {'offerprice':offerprice, 'form':form, 'prodinfo':prodinfo}
    return render(request, 'Order/SetPriceProd.html', context)

@login_required
def OfferPrint(request, pk):
    offerprice = OfferPrice.objects.prefetch_related('Offer_No').select_related('ReqNo').annotate(
        qtytotal=Sum('Offer_No__Qty'),
        copricetotal=Sum(F('Offer_No__CoPrice') * F('Offer_No__Qty')),
        offerpricetotal=Sum(F('Offer_No__OfferPrice') * F('Offer_No__Qty')),
    ).annotate(
        totalmargin =  100 - Cast(F('copricetotal'), FloatField()) / Cast(F('offerpricetotal'), FloatField()) * 100,
        margintotal = F('offerpricetotal') - F('copricetotal')
    ).filter(
        pk=pk
    ).all()

    context = {'offerprice':offerprice}

    #return Render.render('Order/OfferPrint.html',context)

    return render(request, 'Order/OfferPrint.html',context)

@login_required
def OfferOrder(request, pk):
    offerdetail = OfferPriceDetail.objects.select_related('ProdCode').annotate(
        qtytotal=Sum('Qty'),
        copricetotal=Sum(F('CoPrice') * F('Qty')),
    ).filter(
        OfferNo=pk
    ).order_by('ProdCode__VendorCode'
    ).all()

    offer = OfferPrice.objects.filter(pk=pk).all()

    context = {'offerdetail':offerdetail,'offer':offer}

    #return Render.render('Order/OfferPrint.html',context)

    return render(request, 'Order/OfferOrder.html',context)

@login_required
def OrderConfirm(request, pk):
    offerprice = OfferPrice.objects.filter(pk=pk).select_related('Offer_No').all()
    offerstatus = offerprice.values_list('OfferResult', flat=True)
    reqquono = offerprice.values_list("ReqNo__pk", flat=True)


    if offerstatus[0] == 'S':
        OfferPrice.objects.filter(pk=pk).update(OfferResult='O')
        OfferPrice.objects.filter(pk=pk).update(OrderDate=datetime.datetime.now())
        ReqQuotation.objects.filter(pk=reqquono[0]).update(Status='O')
        ReqQuotation.objects.filter(pk=reqquono[0]).update(StatusO_Date=datetime.datetime.now())
        OfferPrice.objects.filter(pk=pk).update(ClosingDate=datetime.datetime.now())
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        return HttpResponse('<script type="text/javascript">alert("상태를 재확인 부탁 드리겠습니다.");window.close();</script>')

@login_required
def OrderList(request):
    orderlist = OfferPrice.objects.prefetch_related('Offer_No').select_related('ReqNo').annotate(
        qtytotal=Sum('Offer_No__Qty'),
        copricetotal=Sum(F('Offer_No__CoPrice') * F('Offer_No__Qty')),
        offerpricetotal=Sum(F('Offer_No__OfferPrice') * F('Offer_No__Qty')),
    ).annotate(
        totalmargin=100 - Cast(F('copricetotal'), FloatField()) / Cast(F('offerpricetotal'), FloatField()) * 100,
        margintotal=F('offerpricetotal') - F('copricetotal')
    ).filter(
        OfferResult = 'O'
    ).all()

    orderlist_filter = OrderListFilter(request.GET, queryset=orderlist)
    context = {'orderlist':orderlist,'orderlist_filter':orderlist_filter}

    return render(request, 'Order/OrderList.html', context)

@login_required
def OrderAddInfo(request, pk):
    post = get_object_or_404(OfferPrice, pk=pk)
    if request.method == 'POST':
        form = OrderAddInfoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = OrderAddInfoForm(instance=post)

    context ={'form':form}

    return render(request, 'Order/OrderAddInfo.html', context)

@login_required
def OrderDetailAddInfo(request, pk):
    post = get_object_or_404(OfferPriceDetail, pk=pk)
    if request.method == 'POST':
        form = OrderDetailAddInfoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = OrderDetailAddInfoForm(instance=post)

    context ={'form':form}

    return render(request, 'Order/OrderDetailAddInfo.html', context)

@login_required
def OfferDelete(request, pk):

    OfferPriceDetail.objects.filter(pk=pk).delete()

    return HttpResponse(
        '<script type="text/javascript">alert("삭제되었습니다.");window.close();opener.location.reload();</script>')

@login_required

def Rental(request):

    rentallist = RentalList.objects.order_by('RentalType').all()

    context = {'rentallist':rentallist}

    return render(request, 'Order/Rental.html', context)

@login_required
def RentalNew(request):
    if request.method == 'POST':
        form = RentalListForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = RentalListForm()

    return render(request, 'Order/new_Rental.html', {'form':form})

@login_required
def RentalEdit(request, pk):
    post = get_object_or_404(RentalList, pk=pk)
    if request.method == 'POST':
        form = RentalListForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = RentalListForm(instance=post)

    return render(request, 'Order/new_Rental.html', {'form':form})