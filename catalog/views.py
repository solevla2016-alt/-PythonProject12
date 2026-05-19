from django.shortcuts import redirect
from catalog.models import Product
from catalog.models import Contact
from django.shortcuts import render, get_object_or_404
from catalog.forms import ProductForm


def home(request):

    products = Product.objects.all()

    return render(
        request,
        "home.html",
        {"products": products}
    )


def contacts(request):

    contacts_list = Contact.objects.all()

    return render(request, "contacts.html", {"contacts": contacts_list})


def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)

    return render(request,"product_detail.html",{"product": product})


def product_create(request):

    if request.method == "POST":

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("catalog:home")

    else:
        form = ProductForm()

    return render(request,"product_form.html",{"form": form})


