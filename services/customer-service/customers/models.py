import uuid
from django.db import models
class Customer(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 user_id=models.UUIDField(unique=True)
 first_name=models.CharField(max_length=100); last_name=models.CharField(max_length=100)
 phone=models.CharField(max_length=30,blank=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
