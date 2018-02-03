from django.shortcuts import render

from . import models
from . import serializers
from django.views.generic.base import TemplateView
from rest_framework import generics
# Create your views here.

class Index(TemplateView):
    template_name = "management/index.html"

class ProviderList(generics.ListCreateAPIView):
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
