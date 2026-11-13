# PyPerfumeStore

A perfume-store application: a Django 5 + Django REST Framework back end with
two apps — a customer-facing store front and a management back office — and
AngularJS 1.x front ends served by Django templates.

The store front (`/`) is the shop; the back office (`/management/`) manages
articles and providers through a small JSON API.

## Requirements

- Python 3.10+ (CI uses 3.12)
- Django 5.2 and Django REST Framework 3.16 — see `Requirements.txt`
- no database server: SQLite is the default

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r Requirements.txt

cd src/PyPerfumeStoreProject
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> for the shop and
<http://127.0.0.1:8000/management/> for the back office.

### Configuration

Everything is read from the environment; nothing secret lives in `settings.py`.

| Variable | Default | Meaning |
|---|---|---|
| `DJANGO_SECRET_KEY` | random per process | signing key — set it in production |
| `DJANGO_DEBUG` | `1` | `0` turns debug off |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | comma-separated hosts |
| `DJANGO_DB_ENGINE` | `sqlite` | `mysql` switches to the original schema |
| `DJANGO_DB_PATH` | `src/PyPerfumeStoreProject/db.sqlite3` | SQLite file |
| `DJANGO_DB_NAME` / `_USER` / `_PASSWORD` / `_HOST` / `_PORT` | `perfume_store_db` / `root` / — / `127.0.0.1` / `3306` | MySQL only |

The random development secret means sessions do not survive a restart; set
`DJANGO_SECRET_KEY` if that matters. For MySQL, uncomment `mysqlclient` in
`Requirements.txt` first.

## The management API

All endpoints are JSON and live under `/management/api/`:

| Method | Path | Behaviour |
|---|---|---|
| `GET` | `/provider` | list providers |
| `POST` | `/provider` | create a provider |
| `GET` | `/article` | list articles, each with its provider nested |
| `POST` | `/article` | create an article |

There is no authentication, pagination, filtering, detail route, update or
delete yet: this is the read/create slice of the back office.

## Data model

`PyPerfumeStoreBackEndApp/models.py` defines the schema the project was written
for, with explicit table names:

| Model | Table | Notes |
|---|---|---|
| `Provider` | `Provider` | name, two address lines, two phone numbers |
| `ArticleType` | `ArticleType` | name and description |
| `ArticleUnit` | `ArticleUnit` | name and description |
| `Article` | `Article` | reference, name, price, quantity, minimum quantity, the three foreign keys, creation date |
| `StoreInfo` | `StoreInfo` | store name and theme colour |

Prices and quantities are `FloatField`s, which is what the original schema
used; decimal money would be the first change to make.

## Tests

```bash
cd src/PyPerfumeStoreProject
python manage.py test
```

7 tests: both pages render, and the provider/article endpoints list, create,
and reject invalid input. `.github/workflows/ci.yml` runs `manage.py check` and
the suite on Python 3.12.

## Layout

```
Requirements.txt
src/PyPerfumeStoreProject/
  manage.py
  PyPerfumeStoreProject/          settings, URLs, WSGI
  PyPerfumeStoreApp/              store front: template, static assets, tests
  PyPerfumeStoreBackEndApp/       back office: models, serializers, DRF views,
                                  templates, migrations, tests
  bower.json                      AngularJS and jQuery dependencies (vendored
                                  under each app's static/bower_components)
```

## License

MIT — see [LICENSE](LICENSE).
