import uuid
from django.db import models
class Notification(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
 user_id=models.UUIDField()
 title=models.CharField(max_length=200)
 message=models.TextField()
 read_at=models.DateTimeField(null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
