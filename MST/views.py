from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .forms import VendorForm, LoginForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from MST.models import CoVendor, CoDept

# Create your views here.
@login_required

def Vendor(request):

    sort = request.GET.get('sort','')

    if sort == 'Contract':
        vendor = CoVendor.objects.order_by('-Contract_YN').all()
        context = {'vendor': vendor}
        return render(request, 'MST/vendor.html', context)
    else:
        vendor = CoVendor.objects.all()
        context = {'vendor':vendor}

    return render(request, 'MST/vendor.html', context)

def Dept(request):
    dept = CoDept.objects.all()
    context = {'dept':dept}

    return render(request, 'MST/dept.html', context)

def VendorNew(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = VendorForm()

    return render(request, 'MST/new_vendor.html', {'form':form})

def VendorEdit(request, pk):
    post = get_object_or_404(CoVendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponse('<script type="text/javascript">alert("저장되었습니다.");window.close();opener.location.reload();</script>')
    else:
        form = VendorForm(instance=post)

    return render(request, 'MST/new_vendor.html', {'form':form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            if user.couser.UserType == 'S':
                return redirect('../Prod/quotation')
            else:
                return redirect('../MST/vendor/')
        else:
            return HttpResponse('로그인 실패')
    else:
        form = LoginForm()
        return render(request, 'MST/login.html',{'form':form})
