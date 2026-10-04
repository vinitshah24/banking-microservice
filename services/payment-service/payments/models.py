import uuid
from django.db import models
class Transfer(models.Model):
 class Status(models.TextChoices): PENDING="PENDING"; COMPLETED="COMPLETED"; FAILED="FAILED"
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 source_account_id=models.UUIDField(); destination_account_id=models.UUIDField(); amount=models.DecimalField(max_digits=20,decimal_places=2); currency=models.CharField(max_length=3)
 idempotency_key=models.CharField(max_length=120,unique=True); status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING); failure_code=models.CharField(max_length=80,blank=True); created_at=models.DateTimeField(auto_now_add=True)
