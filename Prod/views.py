from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ProductForm, ReqQuotaionForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from Prod.models import ReqQuotation, ProductList, ProductInventory
from Order.models import OfferPrice
import datetime
from .filters import ProductOfferFilter

# Create your views here.
@login_required
def Quotation(request):
    quotation = ReqQuotation.objects.all()
    context = {'quotation':quotation}

    return render(request, 'Prod/ReqQuo.html', context)

@login_required
def ProductMaster(request):
    product = ProductList.objects.all()
    product_filter = ProductOfferFilter(request.GET, queryset=product)
    context = {'filter':product_filter,'product':product}

    return render(request, 'Prod/Product.html', context)
@login_required
def Inventory(request):
    inventory = ProductInventory.objects.select_related('Prodcode').all()
    context = {'inventory':inventory}

    return render(request, 'Prod/Inventory.html', context)

@login_required
def ProductNew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = ProductForm()

    return render(request, 'Prod/new_product.html', {'form':form})

@login_required
def ProductEdit(request, pk):
    post = get_object_or_404(ProductList, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = ProductForm(instance=post)

    return render(request, 'Prod/new_product.html', {'form':form})

@login_required
def ReqQuotationNew(request):
    if request.method == 'POST':
        form = ReqQuotaionForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = ReqQuotaionForm()

    return render(request, 'Prod/new_ReqQuotation.html', {'form':form})

def ReqQuotationChange(request, pk):
    OriginReqQuotation = ReqQuotation.objects.filter(pk=pk).all()
    if request.method == 'POST':
        form = ReqQuotaionForm(request.POST, request.POST)
        if form.is_valid():
            OriginReqQuotation.update(Status='C')
            OriginReqQuotation.update(StatusC_Date=datetime.datetime.now())
            form.save()


            return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
        else :
            return HttpResponse(
                '<script type="text/javascript">alert("저장이 실패하였습니다.");window.close();opener.location.reload();</script>')
    else:
        OriginCustname = OriginReqQuotation.values_list('Custname', flat=True)
        OriginDeptCode = OriginReqQuotation.values_list('DeptCode', flat=True)
        OriginEmpNo = OriginReqQuotation.values_list('EmpNo', flat=True)
        OriginReqNo = OriginReqQuotation.values_list('ReqNo', flat=True)
        form = ReqQuotaionForm(initial={"Custname":OriginCustname[0],"EmpNo":OriginEmpNo[0],"DeptCode":OriginDeptCode[0],"OriginReqNo":OriginReqNo[0]})

    return render(request, 'Prod/new_ReqQuotation.html', {'form':form})

@login_required
def ReqQuotationEdit(request, pk):
    post = get_object_or_404(ReqQuotation, pk=pk)
    if request.method == 'POST':
        form = ReqQuotaionForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = ReqQuotaionForm(instance=post)

    return render(request, 'Prod/new_ReqQuotation.html', {'form':form})

@login_required
def SendmailQuotation(request, pk):
    quotation = ReqQuotation.objects.filter(pk=pk).all()
    context = {'quotation':quotation}

    quostatus = quotation.values_list('Status',flat=True)

    if quostatus[0] == 'A':
        ReqQuotation.objects.filter(pk=pk).update(Status='R')
        ReqQuotation.objects.filter(pk=pk).update(StatusR_Date=datetime.datetime.now())
    else:
        return HttpResponse('<script type="text/javascript">alert("접수 상태가 아닙니다.");window.close();opener.location.reload();</script>')
    return render(request, 'Prod/SendMail.html', context)

@login_required
def SearchProductOffer(request, offerpk):
    product_list = ProductList.objects.all()
    offer = OfferPrice.objects.filter(pk=offerpk).all()
    product_filter = ProductOfferFilter(request.GET, queryset=product_list)

    return render(request, 'Prod/SearchProdOffer.html',{'filter':product_filter,'offer':offer})



