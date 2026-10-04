# Django Banking Microservices

A production-minded v1 reference implementation for a banking platform using Django REST Framework.

## Architecture

- auth-service — registration, login, refresh, logout, password change, JWT identity
- customer-service — customer profiles
- account-service — account metadata and balance/transaction read APIs
- ledger-service — immutable double-entry ledger and source-of-truth balances
- payment-service — idempotent transfer orchestration
- notification-service — notification inbox
- audit-service — audit event storage
- nginx — API edge gateway
- PostgreSQL — development database server
- RabbitMQ / Redis — infrastructure reserved for async events and caching

## v1 public endpoints

Auth: POST /api/v1/auth/register, POST /api/v1/auth/login, POST /api/v1/auth/refresh, POST /api/v1/auth/logout, POST /api/v1/auth/change-password, GET /api/v1/auth/me

Customers: POST /api/v1/customers, GET /api/v1/customers, GET /api/v1/customers/{id}, PATCH /api/v1/customers/{id}

Accounts: POST /api/v1/accounts, GET /api/v1/accounts, GET /api/v1/accounts/{id}, PATCH /api/v1/accounts/{id}, GET /api/v1/accounts/{id}/balance, GET /api/v1/accounts/{id}/transactions

Transfers: POST /api/v1/transfers, GET /api/v1/transfers, GET /api/v1/transfers/{id}

A transfer requires an Idempotency-Key header. Money is posted atomically in the ledger as one debit and one credit.

Ledger reads: GET /api/v1/ledger/accounts/{account_id}/entries and GET /api/v1/ledger/entries/{id}. Ledger mutations and ledger-account creation are internal-only under /internal/v1/....

Notifications and audit are exposed as GET /api/v1/notifications and GET /api/v1/audit/events.

## Response contract

Single responses use success, data, meta.request_id, and error. List responses add meta.pagination with page, page_size, total, total_pages, has_next, and has_previous. Errors use stable error.code, error.message, and error.details fields.

## Swagger / OpenAPI

Each Django service uses drf-spectacular. Swagger UI is available at:

- http://localhost:8001/api/docs/ — Auth
- http://localhost:8002/api/docs/ — Customer
- http://localhost:8003/api/docs/ — Account
- http://localhost:8004/api/docs/ — Ledger
- http://localhost:8005/api/docs/ — Payment
- http://localhost:8006/api/docs/ — Notification
- http://localhost:8007/api/docs/ — Audit

Each service also exposes /api/schema/ and /api/redoc/.

## Run

    cp .env.example .env
    docker compose up --build

The gateway is available at http://localhost:8000.

## Banking safety model

The ledger is the source of truth for money. Ledger entries are immutable and transfers are double-entry. The payment service uses idempotency keys and the ledger uses a unique transaction reference to prevent duplicate posting.

This is a reference implementation, not a production banking system. Production deployment should add managed database isolation, secret/key rotation, asymmetric service identity or mTLS, durable outbox/inbox processing, reconciliation, KYC/AML/fraud controls, rate limiting, structured audit trails, disaster recovery, observability, and formal security testing.
