from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts

app_name = CatalogConfig.name

urlpatterns = [path("", index), path("contacts/", contacts)]
