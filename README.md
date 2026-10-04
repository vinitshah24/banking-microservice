# Django Banking Microservices

A production-minded v1 reference architecture for a banking platform built with Django REST Framework, PostgreSQL, RabbitMQ, Redis, JWT authentication, service-to-service authentication, an immutable double-entry ledger, idempotent transfers, generic API envelopes, pagination, and drf-spectacular documentation.

## Services

- auth-service — users, JWT access/refresh tokens
- customer-service — customer profiles
- account-service — bank account metadata
- ledger-service — immutable double-entry ledger and balances
- payment-service — transfer orchestration and idempotency
- notification-service — notification inbox and event consumer
- audit-service — audit event storage and event consumer
- nginx — edge/API gateway

## API conventions

Public APIs use `/api/v1/...` and return:

```json
{"success":true,"data":{},"meta":{"request_id":"..."},"error":null}
```

List responses add `meta.pagination`. Errors use a stable `error.code` and `error.message`.

Swagger/OpenAPI is generated independently by each Django service with drf-spectacular. Each service exposes `/api/schema/`, `/api/docs/`, and `/api/redoc/`.

## Run locally

1. Copy `.env.example` to `.env`.
2. Run `docker compose up --build`.
3. Open the gateway on `http://localhost:8000`.
4. Service docs are exposed on ports 8001-8007.

This repository is a reference implementation, not a substitute for a bank's regulatory, security, fraud, KYC/AML, secrets-management, key-management, disaster-recovery, and operational controls. For production, replace development secrets and add asymmetric service identity or mTLS, managed databases, secret rotation, durable outbox/inbox processing, reconciliation, and stronger observability.
