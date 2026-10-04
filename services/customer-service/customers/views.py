from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from banking_common.api import ok,fail
from .models import Customer
from .serializers import CustomerSerializer
class CustomerListCreate(APIView):
 permission_classes=[IsAuthenticated]
 def get(self,request):
  qs=Customer.objects.order_by("-created_at"); from banking_common.pagination import StandardPagination; p=StandardPagination(); page=p.paginate_queryset(qs,request); return p.get_paginated_response(CustomerSerializer(page,many=True).data)
 def post(self,request):
  data={**request.data,"user_id":str(getattr(request.user,"user_id",request.data.get("user_id")))}
  s=CustomerSerializer(data=data)
  if not s.is_valid(): return fail(request,"VALIDATION_ERROR","Invalid customer data",s.errors)
  return ok(request,CustomerSerializer(s.save()).data,status_code=201)
class CustomerDetail(APIView):
 def get_object(self,pk): return Customer.objects.filter(pk=pk).first()
 def get(self,request,pk):
  obj=self.get_object(pk)
  return ok(request,CustomerSerializer(obj).data) if obj else fail(request,"CUSTOMER_NOT_FOUND","Customer was not found",status_code=404)
 def patch(self,request,pk):
  obj=self.get_object(pk)
  if not obj:return fail(request,"CUSTOMER_NOT_FOUND","Customer was not found",status_code=404)
  s=CustomerSerializer(obj,data=request.data,partial=True)
  if not s.is_valid():return fail(request,"VALIDATION_ERROR","Invalid customer data",s.errors)
  return ok(request,CustomerSerializer(s.save()).data)
