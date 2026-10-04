from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIRequestFactory,force_authenticate
from banking_common.service_auth import ServicePrincipal
from .models import LedgerAccount
from .views import PostTransfer
class LedgerTransferTests(TestCase):
 def setUp(self):
  self.a=LedgerAccount.objects.create(external_account_id="00000000-0000-0000-0000-000000000001",currency="USD")
  self.b=LedgerAccount.objects.create(external_account_id="00000000-0000-0000-0000-000000000002",currency="USD")
 def test_transfer_rejects_insufficient_funds(self):
  request=APIRequestFactory().post("/internal/v1/ledger/transfers",{"source_account_id":str(self.a.external_account_id),"destination_account_id":str(self.b.external_account_id),"amount":"10.00","currency":"USD","reference":"t1"},format="json")
  force_authenticate(request,user=ServicePrincipal("payment-service"))
  response=PostTransfer.as_view()(request)
  self.assertEqual(response.status_code,409)
