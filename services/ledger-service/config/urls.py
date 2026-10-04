from django.urls import path
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView,SpectacularRedocView
from ledger.views import LedgerEntryList,LedgerAccountCreate,PostTransfer,LedgerBalance
urlpatterns=[path("api/v1/ledger/accounts/<uuid:account_id>/entries",LedgerEntryList.as_view()),path("api/v1/ledger/entries/<uuid:pk>",LedgerEntryList.as_view()),path("internal/v1/ledger/accounts",LedgerAccountCreate.as_view()),path("internal/v1/ledger/accounts/<uuid:account_id>/balance",LedgerBalance.as_view()),path("internal/v1/ledger/transfers",PostTransfer.as_view()),path("api/schema/",SpectacularAPIView.as_view()),path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"))]
