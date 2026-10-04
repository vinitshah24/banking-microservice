import uuid
from django.db import models
class AuditEvent(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 actor_id=models.UUIDField(null=True,blank=True)
 service=models.CharField(max_length=80)
 action=models.CharField(max_length=120)
 resource_type=models.CharField(max_length=80)
 resource_id=models.CharField(max_length=120)
 payload=models.JSONField(default=dict)
 created_at=models.DateTimeField(auto_now_add=True)
