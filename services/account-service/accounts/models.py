import uuid
from django.db import models
class Account(models.Model):
 class Status(models.TextChoices): ACTIVE="ACTIVE"; BLOCKED="BLOCKED"; CLOSED="CLOSED"
 class Type(models.TextChoices): CHECKING="CHECKING"; SAVINGS="SAVINGS"
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 customer_id=models.UUIDField(); account_number=models.CharField(max_length=32,unique=True)
 type=models.CharField(max_length=20,choices=Type.choices,default=Type.CHECKING); currency=models.CharField(max_length=3,default="USD")
 status=models.CharField(max_length=20,choices=Status.choices,default=Status.ACTIVE); created_at=models.DateTimeField(auto_now_add=True)
