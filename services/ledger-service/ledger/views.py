from decimal import Decimal
from django.db import transaction
from django.db.models import Sum,Case,When,F,DecimalField
from rest_framework.views import APIView
from banking_common.api import ok,fail
from banking_common.service_auth import ServiceAuthentication
from .models import LedgerAccount,LedgerTransaction,LedgerEntry
from .serializers import LedgerEntrySerializer
class LedgerAccountCreate(APIView):
 authentication_classes=[ServiceAuthentication]
 def post(self,request):
  account_id=request.data.get("account_id"); currency=request.data.get("currency","USD")
  obj,_=LedgerAccount.objects.get_or_create(external_account_id=account_id,defaults={"currency":currency})
  return ok(request,{"id":str(obj.external_account_id),"currency":obj.currency},status_code=201)
class PostTransfer(APIView):
 authentication_classes=[ServiceAuthentication]
 @transaction.atomic
 def post(self,request):
  src,dst=request.data.get("source_account_id"),request.data.get("destination_account_id"); amount=Decimal(str(request.data.get("amount","0"))); currency=request.data.get("currency","USD"); ref=request.data.get("reference")
  if amount<=0 or not ref:return fail(request,"INVALID_TRANSFER","Amount and reference are required")
  if LedgerTransaction.objects.filter(reference=ref).exists(): return ok(request,{"reference":ref,"status":"ALREADY_POSTED"})
  a=LedgerAccount.objects.select_for_update().filter(external_account_id=src).first(); b=LedgerAccount.objects.select_for_update().filter(external_account_id=dst).first()
  if not a or not b:return fail(request,"LEDGER_ACCOUNT_NOT_FOUND","One or more ledger accounts were not found",status_code=404)
  if a.currency!=currency or b.currency!=currency:return fail(request,"CURRENCY_MISMATCH","Transfer currency does not match ledger accounts")
  balance=LedgerEntry.objects.filter(account=a).aggregate(v=Sum(Case(When(direction="CREDIT",then=F("amount")),When(direction="DEBIT",then=-F("amount")),default=0,output_field=DecimalField(max_digits=20,decimal_places=2))))["v"] or Decimal("0")
  if balance<amount:return fail(request,"INSUFFICIENT_FUNDS","Insufficient funds",status_code=409)
  tx=LedgerTransaction.objects.create(reference=ref)
  LedgerEntry.objects.bulk_create([LedgerEntry(transaction=tx,account=a,amount=amount,direction="DEBIT",currency=currency),LedgerEntry(transaction=tx,account=b,amount=amount,direction="CREDIT",currency=currency)])
  return ok(request,{"transaction_id":str(tx.id),"reference":ref,"status":"POSTED"},status_code=201)
class LedgerEntryList(APIView):
 def get(self,request,account_id,pk=None):
  if pk:
   obj=LedgerEntry.objects.filter(pk=pk).first(); return ok(request,LedgerEntrySerializer(obj).data) if obj else fail(request,"ENTRY_NOT_FOUND","Ledger entry was not found",status_code=404)
  from banking_common.pagination import StandardPagination
  qs=LedgerEntry.objects.filter(account__external_account_id=account_id).order_by("-created_at"); p=StandardPagination(); page=p.paginate_queryset(qs,request); return p.get_paginated_response(LedgerEntrySerializer(page,many=True).data)
