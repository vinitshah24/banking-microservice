from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
import uuid
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra):
        if not email: raise ValueError("email required")
        u=self.model(email=self.normalize_email(email),**extra); u.set_password(password); u.save(using=self._db); return u
    def create_superuser(self,email,password=None,**extra):
        extra.update(is_staff=True,is_superuser=True); return self.create_user(email,password,**extra)
class User(AbstractBaseUser,PermissionsMixin):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD="email"
    objects=UserManager()
