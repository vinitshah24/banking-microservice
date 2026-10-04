from rest_framework.views import APIView
from banking_common.api import ok,fail
from banking_common.services import call_service
from .models import Transfer
from .serializers import TransferSerializer
class TransferListCreate(APIView):
 def get(self,request):
  from banking_common.pagination import StandardPagination
  p=StandardPagination(); page=p.paginate_queryset(Transfer.objects.order_by("-created_at"),request); return p.get_paginated_response(TransferSerializer(page,many=True).data)
 def post(self,request):
  key=request.headers.get("Idempotency-Key") or request.data.get("idempotency_key")
  if not key:return fail(request,"IDEMPOTENCY_KEY_REQUIRED","Idempotency-Key is required")
  existing=Transfer.objects.filter(idempotency_key=key).first()
  if existing:return ok(request,TransferSerializer(existing).data)
  s=TransferSerializer(data={**request.data,"idempotency_key":key})
  if not s.is_valid():return fail(request,"VALIDATION_ERROR","Invalid transfer data",s.errors)
  obj=s.save()
  try:
   result=call_service("http://ledger:8000/internal/v1/ledger/transfers","payment-service","POST",{"source_account_id":str(obj.source_account_id),"destination_account_id":str(obj.destination_account_id),"amount":str(obj.amount),"currency":obj.currency,"reference":str(obj.id)})
   obj.status=Transfer.Status.COMPLETED; obj.save(update_fields=["status"])
   return ok(request,TransferSerializer(obj).data,status_code=201)
  except Exception as exc:
   obj.status=Transfer.Status.FAILED; obj.failure_code="LEDGER_REJECTED"; obj.save(update_fields=["status","failure_code"])
   return fail(request,"TRANSFER_FAILED","Transfer could not be posted",{"transfer_id":str(obj.id)},status_code=409)
class TransferDetail(APIView):
 def get(self,request,pk):
  obj=Transfer.objects.filter(pk=pk).first(); return ok(request,TransferSerializer(obj).data) if obj else fail(request,"TRANSFER_NOT_FOUND","Transfer was not found",status_code=404)
