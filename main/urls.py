from django.urls import path

from main.apps import MainConfig
from main.views import product, catalog


app_name = MainConfig.name

urlpatterns = [
    path('product/<int:pk>/', product, name='product'),
    path('', catalog, name='catalog'),
]
