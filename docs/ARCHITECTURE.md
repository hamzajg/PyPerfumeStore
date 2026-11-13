# Architecture — PyPerfumeStore

Current-state map. Descriptive, not aspirational; see `docs/adr/` for why.

## System shape

```
Browser
  ├─ /            → PyPerfumeStoreApp (store front)
  │                  Django template + vendored AngularJS/jQuery (bower)
  └─ /management/  → PyPerfumeStoreBackEndApp (back office)
                     Django template + AngularJS calling /management/api/*
        │
        ▼
Django 5.2 + DRF 3.16
  ├─ PyPerfumeStoreApp/        views.py (Index), templates, static/
  └─ PyPerfumeStoreBackEndApp/ models.py, serializers.py, views.py (DRF),
                               urls.py, templates, migrations/
        │
        ▼
SQLite (default) | MySQL (DJANGO_DB_ENGINE=mysql, legacy schema)
```

## Domain model

`PyPerfumeStoreBackEndApp/models.py` — explicit table names, legacy
PascalCase field names preserved from the original schema:

- `Provider` — name, two address lines, two phone numbers.
- `ArticleType`, `ArticleUnit` — lookup tables (name + description).
- `Article` — reference, name, `FloatField` price/quantity/min-quantity,
  FKs to Provider/ArticleType/ArticleUnit, creation date.
- `StoreInfo` — store name + theme colour (singleton-ish config row).

## API surface

Only the read/create slice exists under `/management/api/`:
`GET/POST provider`, `GET/POST article` (article list nests its provider).
No auth, pagination, filtering, detail routes, update, or delete — the
README states this is intentional current scope.

## Frontend

Server-rendered Django templates + AngularJS 1.x/jQuery loaded from
**vendored** `static/bower_components` (committed; `bower.json` declares
them). There is no Node build pipeline — assets are static files. The
management UI talks to `/management/api/*`; the shop front is largely
static/template-driven.

## Data

- SQLite default (`DJANGO_DB_PATH`, `src/PyPerfumeStoreProject/db.sqlite3`).
- MySQL optional for the original schema; requires `mysqlclient` (commented
  in `Requirements.txt`) and system MySQL headers.
- Settings are 100% env-driven; no secrets in `settings.py`.

## Key decisions (see docs/adr/)

- Two-app split mirroring shop vs back office.
- Legacy schema compatibility over normalization (FloatField money,
  PascalCase fields, explicit table names).
- No build tooling for the frontend — vendored assets keep the project
  Python-only.
