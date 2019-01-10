from django.db import models
from MST.models import CoVendor, CoUser, CoDept, CoEmp
from django.utils import timezone
from django import forms
from project_sb.global_variables import *

# Create your models here.
class ReqQuotation(models.Model):

    def ReqNO_default():
        now = timezone.now()
        nowStr = now.strftime('%Y%m%d-%H%M%S')
        return "RQ"+nowStr

    ReqNo = models.CharField(max_length=30, default=ReqNO_default)               # 요청번호
    OriginReqNo = models.CharField(max_length=20, blank=True)                                           # 원요청번호
    DeptCode = models.ForeignKey(CoDept, on_delete=models.CASCADE, related_name="ReqQ_Dept")            # 부서코드
    EmpNo = models.ForeignKey(CoEmp, on_delete=models.CASCADE, related_name="ReqQ_Emp")                 # 사원번호
    Custname = models.CharField(max_length=100)                                                         # 고객명
    RPCustname = models.CharField(max_length=100, blank=True)                                           # 렌탈사/파트너사
    Rental_YN = models.BooleanField()                                                                   # 렌탈 여부
    Bid_YN = models.BooleanField()                                                                      # 입찰 여부
    ReqProd = models.TextField()                                                                        # 요청 사양
    Remark = models.CharField(max_length=500, blank=True)                                               # 기타 사항
    CanonETC = models.CharField(max_length=500, blank=True) # 캐논 상품 매출
    ShipDT = models.DateField( blank=True, null=True)                                                   # 납품 예상 일자
    ReqDate = models.DateField( blank=True, null=True, default=timezone.now)                            # 요청 일자
    Status = models.CharField(max_length=2, choices=Req_status, default='A',blank=True)                 # 상태
    StatusA_Date = models.DateField(blank=True, null=True, default=timezone.now)                        # 상태일자(A)-접수
    StatusR_Date = models.DateField(blank=True, null=True) # 상태일자(R)-요청일자
    StatusS_Date = models.DateField(blank=True, null=True) # 상태일자(S)
    StatusO_Date = models.DateField(blank=True, null=True) # 상태일자(O)
    StatusC_Date = models.DateField(blank=True, null=True) # 상태일자(C)
    StatusF_Date = models.DateField(blank=True, null=True) # 상태일자(F)
    VendorReq_YN = models.BooleanField(default=False)                                                                # 벤더 요청 여부
    ReqVendor1 = models.ForeignKey(CoVendor, on_delete=models.CASCADE, related_name="ReqVendor1", blank=True, null=True)       # 요청 벤더 1
    ReqVendor2 = models.ForeignKey(CoVendor, on_delete=models.CASCADE, related_name="ReqVendor2", blank=True, null=True) # 요청 벤더 2
    ReqVendor3 = models.ForeignKey(CoVendor, on_delete=models.CASCADE, related_name="ReqVendor3", blank=True, null=True) # 요청 벤더 3
    VendorReqUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name="ReqUser", blank=True, null=True)         # 요청 유저
    # OfferPriceNo = models.ForeignKey() 제외
    # OrderProductNo = models.ForeignKey() 제외
    FailReason = models.CharField(max_length=500, blank=True)                                          # 실패 사유
    RegUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Req_RegUser', null=True, blank=True) # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                      # 등록 일자
    UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Req_UpdateUser', null=True, blank=True) # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                       # 갱신 일자

    def __str__(self):  # __str__ on Python 3
        return self.ReqNo

class ProductList(models.Model):

    ProdDiv = models.CharField(max_length=2, choices=Product_Div)                   # 상품 구뷴
    ProdName = models.CharField(max_length=50)                                                          # 상품명
    ProdBrand = models.CharField(max_length=20)                                                         # 브랜드명
    VendorCode = models.ForeignKey(CoVendor, on_delete=models.CASCADE, related_name='Prod_Vendor')      # 매입사
    Mercury_YN = models.BooleanField(default=False)                                                     # AX 등록여부
    AXProdCode = models.CharField(max_length=10, blank=True)                                            # AX 물품코드
    AXProdName = models.CharField(max_length=50, blank=True)                                            # AX 상품명
    AXRegDate = models.DateField(blank=True, null=True)                                                 # AX 등록일자
    ProdStatus = models.CharField(max_length=1, choices=Product_status)                                 # 상태
    Basic_coprice = models.IntegerField(blank=True, default=0)                                          # 기본 매입가
    Basic_price = models.IntegerField(blank=True, default=0)                                            # 기본 매출가
    Inventory_YN = models.BooleanField(default=False)                                                   # 재고 운영 여부
    Remark = models.TextField(blank=True)                                                               # 기타사항
    RegUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Prod_RegUser', blank=True, null=True) # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                       # 등록일자
    UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Prod_UpdateUser', blank=True, null=True)    # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                        # 갱신일자
    DTType = models.CharField(max_length=2, choices=DT_enumtype, blank=True)                                # 데스크탑 타입
    NTType = models.CharField(max_length=2, choices=NT_enumtype, blank=True)                                # 노트북 타입
    MTType = models.CharField(max_length=2, choices=MT_enumtype, blank=True)                                # 모니터 타입
    ETCType = models.CharField(max_length=50, blank=True)                                               # 기타 타입
    DTCPU = models.CharField(max_length=2, choices=CPU_enumtype, blank=True)                           # CPU 구분
    DTCPUDetail = models.CharField(max_length=10, blank=True)                             # CPU 상세
    NTCPU = models.CharField(max_length=2, choices=CPU_enumtype, blank=True)                           # CPU 구분
    NTCPUDetail = models.CharField(max_length=10, blank=True)                             # CPU 상세
    DTRAM = models.CharField(max_length=1,choices=RAM_enumtype, blank=True, default=2)   # RAM
    DTHDD = models.CharField(max_length=2, choices=HDD_enumtype, blank=True)
    DTSSD = models.CharField(max_length=2, choices=SSD_enumtype, blank=True)
    DTGraphicCard = models.CharField(max_length=20, blank=True, default='내장')       #그래픽카드
    NTRAM = models.CharField(max_length=1,choices=RAM_enumtype, blank=True, default=2)
    NTHDD = models.CharField(max_length=2, choices=HDD_enumtype, blank=True)
    NTSSD = models.CharField(max_length=2, choices=SSD_enumtype, blank=True)
    NTGraphicCard = models.CharField(max_length=20, blank=True)  # 그래픽카드
    DTPower = models.IntegerField(blank=True, default=0)             #파워
    Keyboard_YN = models.BooleanField(blank=True, default=False)       #키보드유무
    DTMouse_YN = models.BooleanField(blank=True, default=False)          #마우스유무
    NTMouse_YN = models.BooleanField(blank=True, default=False)  # 마우스유무
    NTPouch_YN = models.BooleanField(blank=True, default=False)        #파우치유무
    NTBag_YN = models.BooleanField(blank=True, default=False)          #가방유무
    DTIORemark = models.CharField(max_length=200,blank=True)         #입출력단자
    NTIORemark = models.CharField(max_length=200, blank=True)  # 입출력단자
    MTIORemark = models.CharField(max_length=200, blank=True)  # 입출력단자
    MTScreenSize = models.FloatField(blank=True, default=0.0)        # 스크린 사이즈
    NTScreenSize = models.FloatField(blank=True, default=0.0)  # 스크린 사이즈
    DTWeight = models.FloatField(blank=True, default=0)               # 무게
    NTWeight = models.FloatField(blank=True, default=0)  # 무게
    MTWeight = models.FloatField(blank=True, default=0)  # 무게
    SRWeight = models.FloatField(blank=True, default=0)  # 무게
    DTOS = models.CharField(max_length=100, blank=True)  # DT OS
    NTOS = models.CharField(max_length=100, blank=True)  # NT OS
    Warranty = models.CharField(max_length=5, default='1년') # Warranty
    Ratio = models.CharField(max_length=2, choices=Ratio_enumtype, blank=True)  #화면비율
    Resolution = models.CharField(max_length=2, choices=Resolution_enumtype, blank=True)    #해상도
    Panel = models.CharField(max_length=2, choices=Panel_enumtype, blank=True)  #패널타입
    ReqSpeed = models.CharField(max_length=2, choices=ReqSpeed_enumType, blank=True)    #응답속도
    BWRatio = models.CharField(max_length=2, choices=BWRatio_enumtype, blank=True)      #명암비
    SRInputWidth = models.IntegerField(blank=True, default=0)   #투입폭
    SRCuttingSize = models.IntegerField(blank=True, default=0)  #최대매수
    SRCapacity = models.IntegerField(blank=True, default=0)    # 용량
    SRPowerCon = models.IntegerField(blank=True, default=0)    # 소비전력
    DTRemark = models.CharField(max_length=500, blank=True)
    NTRemark = models.CharField(max_length=500, blank=True)
    MTRemark = models.CharField(max_length=500, blank=True)
    SRRemark = models.CharField(max_length=500, blank=True)
    ETCRemark1 = models.CharField(max_length=500, blank=True)    # 기타사양1
    ETCRemark2 = models.CharField(max_length=500, blank=True)    # 기타사양2
    ETCRemark3 = models.CharField(max_length=500, blank=True)  # 기타사양3

    def Margin(self):
        if self.Basic_coprice == 0:
            return 0
        else:
            a = (self.Basic_price - self.Basic_coprice) / self.Basic_price * 100
            return float(("%0.2f"%a))

    def __str__(self):  # __str__ on Python 3
        return self.ProdName

class ProductInventory(models.Model):
    InvenDate = models.DateField()                                                                      # 재고 기준 일자
    Prodcode = models.ForeignKey('ProductList', on_delete=models.CASCADE, )                             # 상품코드
    InvenQty = models.IntegerField(default=0)                                                           # 재고 수량
    Remark = models.CharField(max_length=100, blank=True)                                               # 특이 사항
    RegUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Inven_RegUser')         # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                       # 등록일자
    UpdateUser = models.ForeignKey(CoUser, on_delete=models.CASCADE, related_name='Inven_UpdateUser', blank=True, null=True)   # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                        # 갱신일자

    def __str__(self):  # __str__ on Python 3
        return str(self.Prodcode)