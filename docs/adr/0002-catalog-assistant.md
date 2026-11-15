# ADR 0002 — Catalog assistant endpoint (deterministic intents)

## Status

Accepted — implemented on `feat/catalog-assistant`.

## Context

Queued Phase-2 candidate: "catalog assistant — management-API-backed
chat for article/provider CRUD". The management API exposes only
list/create for Provider and Article; there is no auth, no LLM provider,
and no key management. Same situation as PyGestComm — an LLM chat
endpoint would add vendor dependency + secrets + unbounded generation
over business data for a two-resource API.

## Decision

`POST /management/api/assistant/ask {"question"}` → `{intent, answer,
data}` from `PyPerfumeStoreBackEndApp/assistant.py`, a deterministic
intent mapper over the same ORM the REST API uses:

- `count_articles` / `count_providers`
- `search_articles` — name, ref, provider name (icontains; id/ref for
  digit terms); provider nested via `select_related`
- `search_providers` — name, addresses, phones
- `low_stock` — `ArticleQte <= ArticleMinQte`: the one intent with real
  business value beyond lookup
- `help` / best-effort `search` fallback

Read-only by design — write intents deferred until a confirmation flow
exists (same rule as PyGestComm and stream-weave's tools).

## Consequences

- Zero new dependencies; fully covered by `APITestCase` (7 new tests,
  14 total passing).
- The intent contract is the stable seam — a future LLM maps free text
  onto these intents without touching the endpoint.
- `FloatField` money/quantities untouched (legacy decision stands).
- Regex intents won't parse arbitrary phrasing — accepted limitation,
  documented rather than patched with more patterns.
