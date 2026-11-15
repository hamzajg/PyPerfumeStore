"""Deterministic assistant intents over the catalog (Article/Provider).

The copilot's *tool surface*, not an LLM — same pattern as PyGestComm:
`answer()` maps intents onto ORM queries and returns structured results.
A future model front-end maps free text onto these intents; the contract
stays stable.

Intents (KISS — extend only when a real caller needs it):
  - count_articles / count_providers
  - search_articles   by name, ref, or provider name
  - search_providers  by name, address, phone
  - low_stock         articles at/below ArticleMinQte — the one intent
                      with actual business value beyond lookup
  - help              fallback
"""

import re

from django.db.models import F, Q

from . import models

_COUNT_ARTICLES = re.compile(r"(how many|count|number of|total)\s+articles?", re.IGNORECASE)
_COUNT_PROVIDERS = re.compile(r"(how many|count|number of|total)\s+providers?", re.IGNORECASE)
_LOW_STOCK = re.compile(r"(low stock|running low|below minimum|presque épuis|stock faible|rupture)", re.IGNORECASE)
_SEARCH_ARTICLES = re.compile(
    r"(find|search|lookup|show|get|list)\s+(article|articles|perfume|perfumes)\s*(.*)",
    re.IGNORECASE)
_SEARCH_PROVIDERS = re.compile(
    r"(find|search|lookup|show|get|list)\s+(provider|providers|supplier|suppliers)\s*(.*)",
    re.IGNORECASE)
_ANY_SEARCH = re.compile(r"(find|search|lookup|show|get)\s+(.*)", re.IGNORECASE)


def _article_brief(a):
    return {
        "ArticleId": a.ArticleId,
        "ArticleRef": a.ArticleRef,
        "ArticleName": a.ArticleName,
        "ArticlePrice": a.ArticlePrice,
        "ArticleQte": a.ArticleQte,
        "ArticleMinQte": a.ArticleMinQte,
        "Provider": a.Provider.ProviderFullName if a.Provider else None,
    }


def _provider_brief(p):
    return {
        "ProviderId": p.ProviderId,
        "ProviderFullName": p.ProviderFullName,
        "ProviderPhoneNum1": p.ProviderPhoneNum1,
    }


def _search_articles(term):
    term = term.strip()
    if not term:
        return models.Article.objects.none()
    qs = models.Article.objects.filter(
        Q(ArticleRef__icontains=term)
        | Q(ArticleName__icontains=term)
        | Q(Provider__ProviderFullName__icontains=term)
    )
    if term.isdigit():
        qs = qs | models.Article.objects.filter(
            Q(ArticleId=int(term)) | Q(ArticleRef__icontains=term))
    return qs.distinct()[:20]


def _search_providers(term):
    term = term.strip()
    if not term:
        return models.Provider.objects.none()
    qs = models.Provider.objects.filter(
        Q(ProviderFullName__icontains=term)
        | Q(ProviderAddress1__icontains=term)
        | Q(ProviderAddress2__icontains=term)
        | Q(ProviderPhoneNum1__icontains=term)
        | Q(ProviderPhoneNum2__icontains=term)
    )
    return qs.distinct()[:20]


def _result(intent, answer, data):
    return {"intent": intent, "answer": answer, "data": data}


def _help():
    return _result("help",
        "I can answer questions about the catalog: 'how many articles', "
        "'how many providers', 'find article <name/ref/provider>', "
        "'find provider <name/phone>', 'low stock articles'.",
        None)


def answer(question):
    """Map a question to {intent, answer, data}. Never raises — unknown
    input falls back to help (or a best-effort article search)."""
    if not isinstance(question, str) or not question.strip():
        return _help()

    text = question.strip()

    if _COUNT_ARTICLES.search(text):
        n = models.Article.objects.count()
        return _result("count_articles",
                       f"{n} article{'s' if n != 1 else ''} in the catalog.",
                       {"count": n})

    if _COUNT_PROVIDERS.search(text):
        n = models.Provider.objects.count()
        return _result("count_providers",
                       f"{n} provider{'s' if n != 1 else ''} registered.",
                       {"count": n})

    if _LOW_STOCK.search(text):
        articles = models.Article.objects.filter(
            ArticleQte__lte=F("ArticleMinQte")).select_related(
            "Provider")[:50]
        rows = [_article_brief(a) for a in articles]
        return _result("low_stock",
                       f"{len(rows)} article{'s' if len(rows) != 1 else ''} "
                       "at or below minimum quantity.",
                       {"articles": rows})

    m = _SEARCH_ARTICLES.search(text)
    if m:
        term = m.group(3) or ""
        articles = list(_search_articles(term))
        return _result("search_articles",
                       f"{len(articles)} article{'s' if len(articles) != 1 else ''} "
                       f"matching '{term}'.",
                       {"query": term,
                        "articles": [_article_brief(a) for a in articles]})

    m = _SEARCH_PROVIDERS.search(text)
    if m:
        term = m.group(3) or ""
        providers = list(_search_providers(term))
        return _result("search_providers",
                       f"{len(providers)} provider{'s' if len(providers) != 1 else ''} "
                       f"matching '{term}'.",
                       {"query": term,
                        "providers": [_provider_brief(p) for p in providers]})

    m = _ANY_SEARCH.search(text)
    if m:
        term = m.group(2).strip(" :,-")
        if len(term) >= 2:
            articles = list(_search_articles(term))
            providers = list(_search_providers(term))
            if articles or providers:
                return _result("search",
                               f"Found {len(articles)} article(s), "
                               f"{len(providers)} provider(s) matching '{term}'.",
                               {"query": term,
                                "articles": [_article_brief(a) for a in articles],
                                "providers": [_provider_brief(p) for p in providers]})

    return _help()
