from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from payments.views import TransferListCreate,TransferDetail
urlpatterns=[path("api/v1/transfers",TransferListCreate.as_view()),path("api/v1/transfers/<uuid:pk>",TransferDetail.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
