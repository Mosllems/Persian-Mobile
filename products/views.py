from django.shortcuts import render, get_object_or_404

from .models import Product
from cart.forms import AddToCartProductForm


def list_product(request, brand):
    products = Product.objects.filter(brand__iexact= brand)
    return render(request, 'products/list_view.html', {'products': products})


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail_view.html', {'product': product, "add_to_cart": AddToCartProductForm()})