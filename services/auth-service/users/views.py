from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from banking_common.api import ok,fail
from .serializers import RegisterSerializer,UserSerializer
from .models import User
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        s=RegisterSerializer(data=request.data)
        if not s.is_valid(): return fail(request,"VALIDATION_ERROR","Invalid registration data",s.errors)
        u=s.save(); return ok(request,UserSerializer(u).data,status_code=201)
class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        u=User.objects.filter(email=request.data.get("email")).first()
        if not u or not u.check_password(request.data.get("password","")): return fail(request,"INVALID_CREDENTIALS","Invalid email or password",status_code=401)
        r=RefreshToken.for_user(u); r.access_token["email"]=u.email; r.access_token["user_id"]=str(u.id)
        return ok(request,{"access":str(r.access_token),"refresh":str(r)})
class MeView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request): return ok(request,UserSerializer(request.user).data)
