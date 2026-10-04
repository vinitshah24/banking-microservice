import httpx
from datetime import timedelta
from rest_framework_simplejwt.tokens import AccessToken

def service_token(service_name):
    token = AccessToken()
    token.set_exp(lifetime=timedelta(minutes=2))
    token["token_type"] = "service"
    token["service"] = service_name
    token["aud"] = "internal-service"
    return str(token)

def call_service(url, service_name, method="GET", json=None, timeout=5):
    with httpx.Client(timeout=timeout) as client:
        response = client.request(method, url, json=json, headers={"Authorization": f"Bearer {service_token(service_name)}"})
        response.raise_for_status()
        return response.json()
