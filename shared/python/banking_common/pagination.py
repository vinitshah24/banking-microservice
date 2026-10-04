from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math
class StandardPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100
    def get_paginated_response(self, data):
        size = self.get_page_size(self.request) or self.page.paginator.count or 1
        return Response({"success": True, "data": data, "meta": {"request_id": getattr(self.request, "request_id", None), "pagination": {"page": self.page.number, "page_size": size, "total": self.page.paginator.count, "total_pages": math.ceil(self.page.paginator.count / size) if size else 1, "has_next": self.page.has_next(), "has_previous": self.page.has_previous()}}, "error": None})
