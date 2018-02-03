from django.shortcuts import render

from .models import Article
from .serializers import ArticleSerializer
from django.views.generic.base import TemplateView
from rest_framework import generics
# Create your views here.

class Index(TemplateView):
    template_name = "management/index.html"

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
