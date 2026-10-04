import os
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.getenv("DJANGO_SECRET_KEY","dev")
DEBUG=True
ALLOWED_HOSTS=["*"]
INSTALLED_APPS=["django.contrib.auth","django.contrib.contenttypes","rest_framework","rest_framework_simplejwt.token_blacklist","drf_spectacular","users"]
MIDDLEWARE=["django.middleware.security.SecurityMiddleware","banking_common.middleware.RequestIDMiddleware"]
ROOT_URLCONF="config.urls"
DATABASES={"default":{"ENGINE":"django.db.backends.postgresql","NAME":"banking","USER":"banking","PASSWORD":"banking","HOST":os.getenv("POSTGRES_HOST","postgres"),"PORT":"5432"}}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
AUTH_USER_MODEL="users.User"
REST_FRAMEWORK={"DEFAULT_SCHEMA_CLASS":"drf_spectacular.openapi.AutoSchema","DEFAULT_AUTHENTICATION_CLASSES":["rest_framework_simplejwt.authentication.JWTAuthentication"]}
SPECTACULAR_SETTINGS={"TITLE":"Banking Auth API","VERSION":"1.0.0"}
from datetime import timedelta
SIMPLE_JWT={"ACCESS_TOKEN_LIFETIME":timedelta(minutes=15),"REFRESH_TOKEN_LIFETIME":timedelta(days=7),"SIGNING_KEY":SECRET_KEY,"AUTH_HEADER_TYPES":("Bearer",)}
