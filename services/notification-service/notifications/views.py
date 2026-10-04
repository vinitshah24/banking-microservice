from rest_framework.views import APIView
from banking_common.api import ok,fail
from .models import Notification
from .serializers import NotificationSerializer
class NotificationList(APIView):
 def get(self,request):
  from banking_common.pagination import StandardPagination
  qs=Notification.objects.filter(user_id=getattr(request.user,"user_id",None)).order_by("-created_at")
  p=StandardPagination(); page=p.paginate_queryset(qs,request)
  return p.get_paginated_response(NotificationSerializer(page,many=True).data)
 def post(self,request):
  if not request.auth or request.auth.get("token_type")!="service":
   return fail(request,"FORBIDDEN","Only internal services may create notifications",status_code=403)
  s=NotificationSerializer(data=request.data)
  if not s.is_valid(): return fail(request,"VALIDATION_ERROR","Invalid notification",s.errors)
  return ok(request,NotificationSerializer(s.save()).data,status_code=201)
