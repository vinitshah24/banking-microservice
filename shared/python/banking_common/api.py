import uuid
from rest_framework.response import Response
from rest_framework import status

def request_id(request):
    return getattr(request, "request_id", None) or request.headers.get("X-Request-ID") or f"req_{uuid.uuid4().hex}"

def ok(request, data=None, meta=None, status_code=status.HTTP_200_OK):
    return Response({"success": True, "data": data, "meta": {"request_id": request_id(request), **(meta or {})}, "error": None}, status=status_code)

def fail(request, code, message, details=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response({"success": False, "data": None, "meta": {"request_id": request_id(request)}, "error": {"code": code, "message": message, "details": details or {}}}, status=status_code)
