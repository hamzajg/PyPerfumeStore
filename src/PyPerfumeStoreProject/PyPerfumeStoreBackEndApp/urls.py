from django.urls import path
from PyPerfumeStoreBackEndApp.views import Index

urlpatterns = [
    path('', Index.as_view(), name='management_index'),
]
