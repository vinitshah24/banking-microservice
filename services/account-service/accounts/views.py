import secrets
from rest_framework.views import APIView
from banking_common.api import ok,fail
from banking_common.services import call_service
from .models import Account
from .serializers import AccountSerializer
class AccountListCreate(APIView):
 def get(self,request):
  from banking_common.pagination import StandardPagination
  p=StandardPagination(); page=p.paginate_queryset(Account.objects.order_by("-created_at"),request); return p.get_paginated_response(AccountSerializer(page,many=True).data)
 def post(self,request):
  data={**request.data,"customer_id":str(getattr(request.user,"user_id",request.data.get("customer_id"))),"account_number":f"{secrets.randbelow(10**10):010d}"}
  s=AccountSerializer(data=data)
  if not s.is_valid():return fail(request,"VALIDATION_ERROR","Invalid account data",s.errors)
  obj=s.save()
  try: call_service("http://ledger:8000/internal/v1/ledger/accounts","account-service","POST",{"account_id":str(obj.id),"currency":obj.currency})
  except Exception as exc:
   obj.delete(); return fail(request,"LEDGER_UNAVAILABLE","Could not initialize ledger account",status_code=502)
  return ok(request,AccountSerializer(obj).data,status_code=201)
class AccountDetail(APIView):
 def get(self,request,pk):
  obj=Account.objects.filter(pk=pk).first()
  return ok(request,AccountSerializer(obj).data) if obj else fail(request,"ACCOUNT_NOT_FOUND","Account was not found",status_code=404)
 def patch(self,request,pk):
  obj=Account.objects.filter(pk=pk).first()
  if not obj:return fail(request,"ACCOUNT_NOT_FOUND","Account was not found",status_code=404)
  s=AccountSerializer(obj,data=request.data,partial=True)
  if not s.is_valid():return fail(request,"VALIDATION_ERROR","Invalid account data",s.errors)
  return ok(request,AccountSerializer(s.save()).data)
