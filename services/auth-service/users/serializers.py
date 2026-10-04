from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    class Meta: model=User; fields=("id","email","password")
    def create(self,validated): return User.objects.create_user(**validated)
class UserSerializer(serializers.ModelSerializer):
    class Meta: model=User; fields=("id","email","created_at")
