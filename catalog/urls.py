from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
]
