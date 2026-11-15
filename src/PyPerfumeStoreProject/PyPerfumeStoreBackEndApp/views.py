from django.shortcuts import render

from . import models
from . import serializers
from .assistant import answer as assistant_answer
from django.views.generic.base import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class Index(TemplateView):
    template_name = "management/index.html"

class ProviderList(generics.ListCreateAPIView):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class AssistantAsk(APIView):
    """POST /management/api/assistant/ask {question} — catalog copilot.

    Deterministic read-only intents over Article/Provider (same ORM as the
    REST API). Write intents deferred pending a confirmation flow.
    """

    def post(self, request):
        return Response(assistant_answer(request.data.get("question", "")))
