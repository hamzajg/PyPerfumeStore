# ADR 0001 — Initial architecture

Date: 2026-11-13 (baseline recorded retroactively)
Status: accepted (describes what is built)

## Context

PyPerfumeStore is a perfume-shop app modernised onto Django 5/DRF while
preserving a legacy schema and an AngularJS 1.x frontend. It must run with
zero infrastructure for development.

## Decisions

1. **Django 5.2 LTS + DRF 3.16, minimal requirements.** Only Django and DRF
   in `Requirements.txt`. Rationale: KISS; `mysqlclient` stays commented
   until MySQL is actually used.
2. **Two-app split.** `PyPerfumeStoreApp` (customer shop) vs
   `PyPerfumeStoreBackEndApp` (management UI + JSON API). Rationale: the
   two surfaces have different audiences and lifecycles; the split keeps
   API changes from touching the shop front.
3. **Legacy schema preserved verbatim.** Explicit table names, PascalCase
  field names (`ArticleRef`, `ProviderFullName`), `FloatField` for money
  and quantities. Rationale: the schema and the AngularJS templates predate
  the rewrite; compatibility beats normalization. README flags decimal
  money as the intended first fix when touching pricing.
4. **Server-rendered templates + vendored bower assets.** AngularJS/jQuery
  live in committed `bower_components`; no Node build step. Rationale:
  keeps the project Python-only and reproducible without a JS toolchain.
5. **Env-driven settings, SQLite default.** `DJANGO_DB_ENGINE` switches
  SQLite↔MySQL; secret key random-per-process in dev. Rationale: zero-config
  dev, no secrets in the repo.
6. **API is deliberately read/create only.** `/management/api/*` has no
  auth, pagination, update, or delete. Accepted scope limitation, stated
  plainly in the README — not an accidental gap.

## Consequences

- Any schema "cleanup" (decimal money, snake_case fields) is a breaking
  change for templates and any API consumers — needs an ADR + migration +
  frontend coordination.
- No auth means the management API must not be exposed beyond trusted
  networks until auth exists.
- Vendored assets will age; replacing AngularJS is a separate project.
