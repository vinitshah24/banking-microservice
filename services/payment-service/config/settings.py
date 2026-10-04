import os
SECRET_KEY=os.getenv("DJANGO_SECRET_KEY","dev");DEBUG=True;ALLOWED_HOSTS=["*"]
INSTALLED_APPS=["django.contrib.contenttypes","rest_framework","drf_spectacular","payments"]
MIDDLEWARE=["banking_common.middleware.RequestIDMiddleware"];ROOT_URLCONF="config.urls";DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
DATABASES={"default":{"ENGINE":"django.db.backends.postgresql","NAME":"banking","USER":"banking","PASSWORD":"banking","HOST":os.getenv("POSTGRES_HOST","postgres"),"PORT":"5432"}}
REST_FRAMEWORK={"DEFAULT_SCHEMA_CLASS":"drf_spectacular.openapi.AutoSchema","DEFAULT_AUTHENTICATION_CLASSES":["banking_common.jwt_auth.ServiceOrUserJWTAuthentication"],"DEFAULT_PERMISSION_CLASSES":["rest_framework.permissions.IsAuthenticated"],"DEFAULT_PAGINATION_CLASS":"banking_common.pagination.StandardPagination"}
SPECTACULAR_SETTINGS={"TITLE":"Banking Payment API","VERSION":"1.0.0"}
