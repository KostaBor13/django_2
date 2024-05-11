from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'base.html', context)


def product_detail(request, pk):
    product_pk = get_object_or_404(Product, pk=pk)
    context = {"product": product_pk}
    return render(request, 'product_detail.html', context)


# def index(request):
#     return render(request, "catalog/home.html")
#
#
# def contacts(request):
#     return render(request, "catalog/contacts.html")
