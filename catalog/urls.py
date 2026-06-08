from django.urls import path

from catalog.apps import CatalogConfig
from .views import (
    HomeListView,
    ContactsTemplateView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [

    path(
        "",
        HomeListView.as_view(),
        name="home"
    ),

    path(
        "contacts/",
        ContactsTemplateView.as_view(),
        name="contacts"
    ),

    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail"
    ),

    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product_create"
    ),

    path(
        "products/update/<int:pk>/",
        ProductUpdateView.as_view(),
        name="product_update"
    ),

    path(
        "products/delete/<int:pk>/",
        ProductDeleteView.as_view(),
        name="product_delete"
    ),
]
