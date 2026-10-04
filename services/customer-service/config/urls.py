from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from customers.views import CustomerListCreate,CustomerDetail
urlpatterns=[path("api/v1/customers",CustomerListCreate.as_view()),path("api/v1/customers/<uuid:pk>",CustomerDetail.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
