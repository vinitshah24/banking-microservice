from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from notifications.views import NotificationList
urlpatterns=[path("api/v1/notifications",NotificationList.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
