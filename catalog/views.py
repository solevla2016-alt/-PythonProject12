from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
)

from catalog.models import Product
from catalog.forms import ProductForm


class HomeListView(ListView):

    model = Product

    template_name = "home.html"

    context_object_name = "products"


class ContactsTemplateView(TemplateView):

    template_name = "contacts.html"


class ProductDetailView(DetailView):

    model = Product

    template_name = "product_detail.html"

    context_object_name = "product"


class ProductCreateView(CreateView):

    model = Product

    form_class = ProductForm

    template_name = "product_form.html"

    success_url = reverse_lazy("catalog:home")


