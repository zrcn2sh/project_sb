from django.db import models
from django.contrib.auth.models import User
from project_sb.global_variables import *
from django.utils import timezone

# Create your models here.

class CoVendor(models.Model):
    # id는 자동생성
    # VendorCode = models.CharField(max_length=7, default='V'+id)     # 매입사 코드,자동 순번으로 대응 가능한지 확인
    CompanyName = models.CharField(max_length=50, )   # 매입사명
    Chief = models.CharField(max_length=30)         # 대표자명
    Address = models.CharField(max_length=100)      # 매입사 주소
    ComNumber = models.CharField(max_length=20, unique=True, error_messages={'unique':'동일한 사업자 번호가 존재합니다.'})     # 사업자 번호
    ComTel = models.CharField(max_length=20)        # 연락처
    Brand = models.CharField(max_length=30)         # 취급 브랜드
    Major_YN = models.BooleanField(default=False)                # 주요 매입사
    ContactName1 = models.CharField(max_length=30)  # 담당자1 이름
    ContactTel1 = models.CharField(max_length=30)   # 담당자1 연락처
    ContactCTel1 = models.CharField(max_length=30)  # 담당자1 핸드폰
    ContactMail1 = models.EmailField()              # 담당자1 이메일
    ContactName2 = models.CharField(max_length=30, blank=True, null=True)  # 담당자2 이름
    ContactTel2 = models.CharField(max_length=30, blank=True, null=True)   # 담당자2 연락처
    ContactCTel2 = models.CharField(max_length=30, blank=True, null=True)  # 담당자2 핸드폰
    ContactMail2 = models.EmailField( blank=True, null=True)              # 담당자2 이메일
    AccountNo = models.CharField(max_length=50, blank=True, null=True)     # 계좌번호
    Status = models.CharField(max_length=1, choices=Vendor_status, default=1)         # 매입사 상태
    PaymentMethod = models.CharField(max_length=30, blank=True, null=True) # 지불방법
    PaymentPeriod = models.CharField(max_length=30, blank=True, null=True) # 지불 기간
    Contract_YN = models.BooleanField( blank=True, null=True, default=False)             # 계약서 체결여부
    ContractDate = models.DateField( blank=True, null=True)               # 계약체결일자
    Remark = models.TextField( blank=True, null=True)                     # 기타(특이사항, 참고사항)
    ComPaper = models.FileField( blank=True, null=True, upload_to='vendor')                   # 사업자 등록증 사본
    AccountPaper = models.FileField(blank=True, null=True, upload_to='vendor')               # 통장 사본
    RegUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoVendor_RegUser', null=True, blank=True)    # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                       # 등록일자
    UpdateUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoVendor_UpdateUser', null=True, blank=True)  # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                            # 갱신일자

    def __unicode__(self): # __str__ on Python 3
        return self.CompanyName

    def __str__(self):
        return self.CompanyName

class CoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)            # 사용자명
    UserName = models.CharField(max_length=20, blank=True, null=True)
    EmpNo = models.ForeignKey('CoEmp', on_delete=models.CASCADE, null=True, blank=True)           # 사원코드
    VendorCode = models.ForeignKey('CoVendor', on_delete=models.CASCADE, null=True, blank=True)   # 매입사 코드
    Email = models.EmailField(blank=True)
    Phone = models.CharField(max_length=20,blank=True)
    UserType = models.CharField(max_length=1, choices=UserType_enumtype)  # 사용자 구분
    LastDate = models.DateField(auto_now=True, null=True, blank=True)                                           # 최종 로그인
    LoginIP = models.CharField(max_length=15, blank=True, null=True)                               # 로그인 IP
    LoginCount = models.IntegerField( null=True)                                      # 로그인 카운터
    RegUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoUser_RegUser', blank=True, null=True)          # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                           # 등록일자
    UpdateUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoUser_UpdateUser', blank=True, null=True)    # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                            # 갱신일자

    def __unicode__(self): # __str__ on Python 3
        return self.UserName

    def __str__(self):
        return self.UserName

class CoDept(models.Model):
    DeptCode = models.CharField(max_length=7)                                                               # 부서코드
    DeptName = models.CharField(max_length=20)                                                              # 부서명
    RegUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoDept_RegUser',null=True, blank=True)          # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                           # 등록일자
    UpdateUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoDept_UpdateUser', null=True, blank=True)    # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                            # 갱신일자

    def __unicode__(self):  # __str__ on Python 3
        return self.DeptName

    def __str__(self):
        return self.DeptName

class CoEmp(models.Model):
    EmpCode = models.CharField(max_length=6)                                                                # 사번
    EmpName = models.CharField(max_length=20)                                                               # 성명
    Dept = models.ForeignKey('CoDept', on_delete=models.CASCADE, related_name='CoEmp_Dept', blank=True, null=True)                 # 부서코드
    RegUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoEmp_RegUser', null=True, blank=True)           # 등록 사용자
    RegDate = models.DateField(auto_now_add=True)                                                           # 등록일자
    UpdateUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoEmp_UpdateUser', null=True, blank=True)     # 갱신 사용자
    UpdateDate = models.DateField(auto_now=True)                                                            # 갱신일자

    def __unicode__(self):  # __str__ on Python 3
        return self.EmpName

    def __str__(self):
        return self.EmpName

class CoDevBoard(models.Model):
    MenuDiv = models.CharField(max_length=20, choices=DevBBSMenuDiv_enumtype)
    MenuName = models.CharField(max_length=50)
    RequestName = models.CharField(max_length=50)
    RequestDetail = models.TextField()
    ReqUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoEmp_ReqUser')
    ReqDate = models.DateField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=DevBBSStatus_enumtype)
    Priority = models.CharField(max_length=5, choices=DevPriority_enumtype)
    Difficulty = models.CharField(max_length=5, choices=DevDifficulty_enumtype)
    RegDate = models.DateField(auto_now_add=True)
    UpdateDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.RequestName

class CoDevBoardReply(models.Model):
    CoDevBoard = models.ForeignKey('CoDevBoard', on_delete=models.CASCADE, related_name='CoDevBoardReply_Board')
    ReplyDetail = models.TextField()
    RegUser = models.ForeignKey('CoUser', on_delete=models.CASCADE, related_name='CoDevBoardReply_RegUser')
    RegDate = models.DateField(auto_now_add=True)
    Version = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.CoDevBoard









