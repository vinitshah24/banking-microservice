from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
class ServiceAuthentication(BaseAuthentication):
    def authenticate(self, request):
        value = request.headers.get("Authorization", "")
        if not value.startswith("Bearer "): return None
        try:
            token = AccessToken(value.split(" ", 1)[1])
            if token.get("token_type") != "service": return None
            if token.get("aud") != "internal-service": raise AuthenticationFailed("Invalid service audience")
            return (ServicePrincipal(token.get("service", "unknown")), token)
        except Exception as exc:
            raise AuthenticationFailed("Invalid service token") from exc
class ServicePrincipal:
    is_authenticated = True
    def __init__(self, name): self.service_name = name
