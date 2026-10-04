from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken

class TokenPrincipal:
    is_authenticated = True
    def __init__(self, token):
        self.user_id = token.get("user_id") or token.get("sub")
        self.email = token.get("email")
        self.token = token

class ServiceOrUserJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        value = request.headers.get("Authorization", "")
        if not value.startswith("Bearer "):
            return None
        try:
            token = AccessToken(value.split(" ", 1)[1])
            if token.get("token_type") == "service":
                return (TokenPrincipal(token), token)
            return (TokenPrincipal(token), token)
        except Exception as exc:
            raise AuthenticationFailed("Invalid access token") from exc
