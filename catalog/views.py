from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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


class ProductCreateView(LoginRequiredMixin, CreateView):

    model = Product

    form_class = ProductForm

    template_name = "product_form.html"

    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Product

    form_class = ProductForm

    template_name = "product_form.html"

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy(
            "catalog:product_detail",
            kwargs={"pk": self.object.pk}
        )


class ProductDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):

    model = Product

    template_name = "product_confirm_delete.html"

    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        product = self.get_object()

        return (
            product.owner == self.request.user
            or
            self.request.user.has_perm(
                "catalog.can_unpublish_product"
            )
        )