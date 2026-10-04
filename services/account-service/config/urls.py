from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from accounts.views import AccountListCreate,AccountDetail
urlpatterns=[path("api/v1/accounts",AccountListCreate.as_view()),path("api/v1/accounts/<uuid:pk>",AccountDetail.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
