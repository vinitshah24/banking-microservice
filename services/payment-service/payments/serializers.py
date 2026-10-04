from rest_framework import serializers
from .models import Transfer
class TransferSerializer(serializers.ModelSerializer):
 class Meta: model=Transfer; fields="__all__"; read_only_fields=("id","status","failure_code","created_at")
