import uuid
from decimal import Decimal
from django.db import models
class LedgerAccount(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 external_account_id=models.UUIDField(unique=True); currency=models.CharField(max_length=3); created_at=models.DateTimeField(auto_now_add=True)
class LedgerTransaction(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 reference=models.CharField(max_length=100,unique=True); created_at=models.DateTimeField(auto_now_add=True)
class LedgerEntry(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 transaction=models.ForeignKey(LedgerTransaction,on_delete=models.PROTECT,related_name="entries")
 account=models.ForeignKey(LedgerAccount,on_delete=models.PROTECT,related_name="entries")
 amount=models.DecimalField(max_digits=20,decimal_places=2)
 direction=models.CharField(max_length=6,choices=[("DEBIT","DEBIT"),("CREDIT","CREDIT")])
 currency=models.CharField(max_length=3); created_at=models.DateTimeField(auto_now_add=True)
