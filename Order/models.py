from django.db import models
from MST.models import CoUser, CoDept, CoEmp, CoVendor
from Prod.models import ProductList, ReqQuotation
from django.utils import timezone
from project_sb.global_variables import *
import datetime
from dateutil.relativedelta import *

# Create your models here.

class OfferPrice(models.Model):

    def OfferNO_default():
        now = timezone.now()
        nowStr = now.strftime('%Y%m%d-%H%M%S')
        return "OF"+nowStr

    OfferNo = models.CharField(max_length=20, default=OfferNO_default)               # 제안번호
    OriginOfferNO = models.CharField(max_length=20, blank=True)                                                     # 원제안번호
    ReqNo = models.ForeignKey(ReqQuotation, on_delete=models.CASCADE, related_name="Offer_ReqNO", null=True)     # 견적 요청 번호
    OfferDate = models.DateField(default=timezone.now)                                                   # 제안 일자
    OfferResult = models.CharField(max_length=5, choices=Offer_status, default='S')                                   # 제안 결과
    OrderDate = models.DateField(blank=True, null=True)
    ClosingDate = models.DateField(blank=True, null=True)
    # 발주 관련 정보 추가 시작
    PONumber = models.CharField(max_length=10, blank=True)                                              # PO번호
    SignNumber = models.CharField(max_length=20, blank=True)                                            # 전자결재번호
    PZNumber = models.CharField(max_length=20, blank=True)
    #Acceptance_YN = models.BooleanField(default=False)                                                  # 인수증 발송 여부
    #AcceptanceDate = models.DateField(blank=True, null=True)                                            # 인수증 발송일자
    #AcceptanceFile = models.FileField(blank=True)                                                       # 인수증 회신 파일
    # 끝
    Quotation = models.FileField(blank=True)                                                            # 견적서 등록
    ReqUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="Offer_RegUser",blank=True, null=True)         # 등록 사용자
    RegDate = models.DateField(auto_now_add=True, null=True)                                            # 등록 일자
    UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="Offer_UpdateUser" ,blank=True, null=True)   # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True, null=True)                                 # 갱신 일자

    def __str__(self):  # __str__ on Python 3
        return self.OfferNo

class OfferPriceDetail(models.Model):
    OfferNo = models.ForeignKey("OfferPrice", on_delete=models.CASCADE, related_name="Offer_No", null=True)        # 제안번호
    #OfferNoSeq = models.IntegerField(blank=True, default=1)                                         # 제안번호-순번
    ProdCode = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name="Offer_Prod")      # 상품코드
    Qty = models.IntegerField()                                                                         # 수량
    CoPrice = models.IntegerField()                                                                     # 매입 단가
    OfferPrice = models.IntegerField()                                                                  # 제안 단가

    # 주문정보 추가 시작
    #DeliveryDate = models.DateField(blank=True)  # 배송요청일
    #Address = models.CharField(max_length=500, blank=True, default='')  # 배송주소
    #ContactPerson = models.CharField(max_length=50, blank=True, default ='')  # 수령인
    #ContactTel = models.CharField(max_length=50, blank=True, default = '')  # 연락처
    #ReleaseDate = models.DateField(blank=True, default=timezone.now)  # 배송요청일
    #DeliveryTempDate = models.DateField(blank=True, default=timezone.now)  # 예상납품일자
    DeliveryDate = models.DateField(blank=True, null=True)  # 납품일자
    LogiType = models.CharField(max_length=4, choices=LogiType_enumtype, blank=True)  # 배송방법
    LogiCompany = models.CharField(max_length=4, choices=LogiCompany_enumtype, blank=True)  # 배송업체
    LogiNo = models.CharField(max_length=50, blank=True)  # 송장번호
    SerialNumber = models.TextField(blank=True, null=True) # 시리얼 번호
    # 끝

    #ReqUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="OfferD_RegUser")        # 등록 사용자
    #RegDate = models.DateField(auto_now_add=True, null=True)                                            # 등록 일자
    #UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="OfferD_UpdateUser",blank=True, null=True)  # 갱신 사용자
    #UpdateDate = models.DateField(auto_now=True, null=True)                                             # 갱신 일자


    def _CoPriceSum(self):
        return int(self.CoPrice * self.Qty)
    CoPriceSum = property(_CoPriceSum)

    def _OfferPriceSum(self):
        return int(self.OfferPrice * self.Qty)

    OfferPriceSum = property(_OfferPriceSum)

    def _MarginSum(self):
        return int(self.OfferPriceSum - self.CoPriceSum)

    MarginSum = property(_MarginSum)

    def _Margin(self):
        if self.CoPrice == 0:
            return 0
        else:
            a = (self.OfferPriceSum - self.CoPriceSum) / self.OfferPriceSum * 100
            return float(("%0.2f"%a))

    Margin = property(_Margin)

    def __str__(self):
        return str(self.OfferNo)

class RentalList(models.Model):

    def RentalNo_default():
        now = timezone.now()
        nowStr = now.strftime('%Y%m%d-%H%M%S')
        return "RT"+nowStr

    RentalNo = models.CharField(max_length=20, default=RentalNo_default) # 관리번호
    RentalType = models.CharField(max_length=1, choices=RentalType_enumtype, default='S') # 렌탈구분
    RentalStatus = models.CharField(max_length=1, choices=RentalStatus_enumtype, default='I') # 진행상태

    DeptCode = models.ForeignKey(CoDept, on_delete=models.CASCADE, related_name="Rental_Dept")  # 부서코드
    EmpNo = models.ForeignKey(CoEmp, on_delete=models.CASCADE, related_name="Rental_Emp")  # 사원번호
    Custname = models.CharField(max_length=100)  # 고객명
    RentalVendor = models.ForeignKey(CoVendor, on_delete=models.CASCADE, related_name="RentalVendor") # 렌탈사
    RentalStartDate = models.DateField() # 렌탈시작일
    RentalPeriod = models.IntegerField(default=1) # 렌탈기간

    RentalProdCode = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name='Rental_Prod')      # 상품코드
    RentalQty = models.IntegerField() # 수량
    RentalCoPrice = models.IntegerField() # 매입단가(월청구매입금액)
    RentalOfferPrice = models.IntegerField() # 매출단가(월청구매출금액)

    ReqUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="Rental_RegUser",blank=True, null=True) # 등록 사용자
    RegDate = models.DateField(auto_now_add=True, null=True)                                            # 등록 일자
    UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="Rental_UpdateUser" ,blank=True, null=True)   # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True, null=True)                                 # 갱신 일자

    def _CoPriceSum(self):
        return int(self.RentalCoPrice * self.RentalQty)
    CoPriceSum = property(_CoPriceSum)

    def _OfferPriceSum(self):
        return int(self.RentalOfferPrice * self.RentalQty)

    OfferPriceSum = property(_OfferPriceSum)

    def _MarginSum(self):
        return int(self.OfferPriceSum - self.CoPriceSum)

    MarginSum = property(_MarginSum)

    def _Margin(self):
        if self.RentalCoPrice == 0:
            return 0
        else:
            a = (self.OfferPriceSum - self.CoPriceSum) / self.OfferPriceSum * 100
            return float(("%0.2f"%a))

    Margin = property(_Margin)

    def _RentalEndDate(self):
        return self.RentalStartDate + relativedelta(months=self.RentalPeriod) - relativedelta(days=1)

    RentalEndDate = property(_RentalEndDate)

    def _RentalRemainMonth(self):
        remain = relativedelta(self.RentalEndDate, datetime.datetime.now())
        return remain.months + remain.years * 12

    RentalRemainMonth = property(_RentalRemainMonth)

    def __str__(self):
        return str(self.RentalNo)