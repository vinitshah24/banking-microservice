from rest_framework.views import APIView
from banking_common.api import ok,fail
from .models import AuditEvent
from .serializers import AuditSerializer
class AuditList(APIView):
 def get(self,request):
  from banking_common.pagination import StandardPagination
  p=StandardPagination(); page=p.paginate_queryset(AuditEvent.objects.order_by("-created_at"),request)
  return p.get_paginated_response(AuditSerializer(page,many=True).data)
 def post(self,request):
  if not request.auth or request.auth.get("token_type")!="service":
   return fail(request,"FORBIDDEN","Only internal services may create audit events",status_code=403)
  s=AuditSerializer(data=request.data)
  if not s.is_valid(): return fail(request,"VALIDATION_ERROR","Invalid audit event",s.errors)
  return ok(request,AuditSerializer(s.save()).data,status_code=201)
