from django.urls import path
from PyPerfumeStoreBackEndApp import views

urlpatterns = [
    path('', views.Index.as_view(), name='management_index'),
    path('api/article', views.ArticleList.as_view()),
]
