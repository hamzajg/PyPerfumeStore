from django.urls import path
from PyPerfumeStoreApp.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
