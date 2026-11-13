# AGENTS.md — PyPerfumeStore

Guidance for AI agents (and humans) working in this repository.

## Project

PyPerfumeStore is a perfume-store app: a Django 5 + DRF backend with two
apps — a customer-facing store front (`/`) and a management back office
(`/management/`) — with AngularJS 1.x + jQuery front ends served through
Django templates and vendored bower components.
Stack: Python 3.10+ (CI uses 3.13), Django 5.2 LTS, DRF 3.16, SQLite
default (MySQL optional via `DJANGO_DB_ENGINE=mysql`).

## Commands

Verified 2026-11-13 against CI (`.github/workflows/ci.yml`) and README.
Note: requirements file is `Requirements.txt` (capital R).

| Task | Command |
|---|---|
| Install deps | `pip install -r Requirements.txt` |
| Migrate | `cd src/PyPerfumeStoreProject && python manage.py migrate` |
| Run dev server | `python manage.py runserver` → shop at `/`, back office at `/management/` |
| Test | `python manage.py test` (7 tests) |
| Django checks | `python manage.py check` |

Requires: env config per README table (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`,
`DJANGO_ALLOWED_HOSTS`, `DJANGO_DB_*`). Defaults work for local dev.
MySQL needs `mysqlclient` uncommented in `Requirements.txt` (system MySQL
headers required).

## Architecture

Django project at `src/PyPerfumeStoreProject/`:

- `PyPerfumeStoreProject/` — `settings.py` (env-driven), `urls.py`, `wsgi.py`.
- `PyPerfumeStoreApp/` — store front: `views.py` (`Index`), templates,
  `static/bower_components` (vendored AngularJS/jQuery/lodash — **committed
  to the repo**, don't npm-install over it).
- `PyPerfumeStoreBackEndApp/` — back office: `models.py` (Provider,
  ArticleType, ArticleUnit, Article, StoreInfo), `serializers.py`,
  `views.py` (DRF lists), `urls.py`, templates, `migrations/`.
- `manage.py` at `src/PyPerfumeStoreProject/manage.py`.

### API contract (frontend ↔ backend)

All JSON endpoints live under `/management/api/` (no auth, no pagination,
no update/delete — read/create slice only):

| Method | Path | Behaviour |
|---|---|---|
| GET/POST | `/management/api/provider` | list / create providers |
| GET/POST | `/management/api/article` | list (provider nested) / create articles |
| GET | `/management/` | back-office HTML page |
| GET | `/` | shop HTML page |

Models (`PyPerfumeStoreBackEndApp/models.py`, explicit table names):
`Provider`, `ArticleType`, `ArticleUnit`, `Article` (FKs to the three +
price/qty as `FloatField`), `StoreInfo` (name + theme colour).

## Conventions

- Two-app split: `PyPerfumeStoreApp` = customer front, `PyPerfumeStoreBackEndApp`
  = management + API. Keep the boundary — store-front changes don't touch
  the API app.
- Model field names are legacy PascalCase-ish (`ArticleRef`,
  `ProviderFullName`) matching the original schema — preserve them; the
  AngularJS templates and any external consumers depend on the shape.
- DRF generic views + `ModelSerializer`s; keep it that simple.
- KISS: requirements are deliberately just Django + DRF; vendored bower
  assets mean **no Node build step exists** — don't introduce one.

## Landmines

- **Default branch is `master`, not `main`.**
- `Requirements.txt` capital-R; `pip install -r requirements.txt` fails
  on case-sensitive filesystems.
- `FloatField` for money/quantities — README flags decimal money as "the
  first change to make"; it's a deliberate legacy choice, not a bug to
  silently fix.
- bower_components are vendored and committed — huge tree; exclude from
  searches and don't "clean them up".
- `DJANGO_SECRET_KEY` defaults to random-per-process → sessions don't
  survive restart in dev; set it if that matters.
- URLs file has commented-out `admin/` — admin is disabled; don't assume
  `/admin/` works.
- MySQL path requires system headers for `mysqlclient` — CI only exercises
  SQLite.

## Agent rules

- Branch from `master`; name branches `feat/*`, `fix/*`, `chore/*`, `docs/*`.
- Docs-only changes still go through a PR; never commit to `master` directly.
- Verify before claiming: run `python manage.py test` from
  `src/PyPerfumeStoreProject` and report the real result.
- Keep changes minimal and consistent with surrounding code. No drive-by
  refactors.
- Update AGENTS.md / docs/ARCHITECTURE.md when your change alters commands,
  models/fields, routes, or the FE/BE contract.
