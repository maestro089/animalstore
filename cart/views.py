from django.shortcuts import render, redirect

from cart.models import Cart, ProductInOrder, Order
from store.models import Product


def get(request):
    price = 0

    cart = Cart.objects.filter(customer=request.user)

    for cart in cart:
        price_product = Product.objects.get(title=cart.title)
        price = price + price_product.price * cart.quentity

    cart = Cart.objects.filter(customer=request.user)

    context = {
        "cart": cart,
        "price": price,
    }
    return render(request, "cart/cart_view.html", context=context)


def add_cart(request):
    path = request.GET.get("next")

    if request.method == "POST":
        if request.POST.get("quentity"):
            Cart.objects.create(
                title=Product.objects.get(id=request.GET.get("product_id")),
                customer=request.user,
                quentity=request.POST.get("quentity"),
            )
    return redirect(path)


def delete_cart(request):
    path = request.GET.get("next")

    if request.method == "POST":
        product = request.GET.get("cart_id")
        cart = Cart.objects.get(id=product)
        cart.delete()
    return redirect(path)


def order(request):
    orders = Order.objects.filter(customer=request.user).order_by("-id")
    product = ProductInOrder.objects.all()

    context = {
        "orders": orders,
        "product": product,
    }
    return render(request, "Order.html", context=context)


def place_order(request):
    list = ""
    cart = Cart.objects.filter(customer=request.user)
    if len(cart) > 0:
        order = Order.objects.create(customer=request.user)

        for cart in cart:
            product = Product.objects.get(pk=cart.title.pk)
            quantity = cart.quentity
            ProductInOrder.objects.create(
                order=order, product=cart.title, quantity=quantity
            )
            cart.delete()
        for b in ProductInOrder.objects.filter(order=order):
            list = list + str(b.product.title) + " Количество " + str(b.quantity) + "\n"
        email_body = "Заказчик: " + str(request.user) + "\n" + list

        return render(request, "cart/cart_view.html")
    return render(request, "cart/cart_view.html")
