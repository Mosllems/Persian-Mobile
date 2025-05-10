from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _
from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item["product_update_quantity_form"] = AddToCartProductForm(initial={
            "quantity": item["quantity"],
            "inplace": True
        })

    return render(request, "cart/cart_detail.html", {
        'cart': cart
    })


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data["quantity"]
        replace_current_quantity = cleaned_data["inplace"]
        cart.add(product, quantity, replace_current_quantity)
    return redirect("home")


def delete_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("home")


def clear_form(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, _("Your cart has been cleared successfully"))
    return redirect("home")

