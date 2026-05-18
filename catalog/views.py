from django.shortcuts import render
from catalog.models import Product
from catalog.models import Contact
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def home(request):
    # последние 5 продуктов
    latest_products = Product.objects.order_by("-created_at")[:5]

    # вывод в консоль (терминал runserver)
    for product in latest_products:
        print(product.name, product.price)

    return render(request, "home.html", {"latest_products": latest_products})


def contacts(request):
    contacts = Contact.objects.all()

    return render(request, "contacts.html", {"contacts": contacts})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request,"product_detail.html",{"product": product})


