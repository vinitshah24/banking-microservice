from rest_framework import serializers
from .models import AuditEvent
class AuditSerializer(serializers.ModelSerializer):
 class Meta:
  model=AuditEvent
  fields="__all__"
