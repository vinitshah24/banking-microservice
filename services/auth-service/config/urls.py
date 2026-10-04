from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from users.views import RegisterView, LoginView, MeView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns=[path("api/v1/auth/register",RegisterView.as_view()),path("api/v1/auth/login",LoginView.as_view()),path("api/v1/auth/refresh",TokenRefreshView.as_view()),path("api/v1/auth/me",MeView.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
