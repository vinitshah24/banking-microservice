from django.test import TestCase
from .models import Transfer
class TransferIdempotencyTests(TestCase):
 def test_idempotency_key_is_unique(self):
  Transfer.objects.create(source_account_id="00000000-0000-0000-0000-000000000001",destination_account_id="00000000-0000-0000-0000-000000000002",amount="1.00",currency="USD",idempotency_key="same")
  self.assertTrue(Transfer.objects.filter(idempotency_key="same").exists())
