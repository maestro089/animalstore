from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from store.models import *
from .forms import *
from news.models import News
from cart.models import Order, ProductInOrder


def index(request):
    return render(request, "admin_panel/index.html")


def moderator_main(request):
    if request.user.is_staff:
        products = CommentsProduct.objects.all()
        user = User.objects.all()

        context = {"products": products, "user": user}

        return render(request, "moderator/moderator_main.html", context=context)
    else:
        return render(request, "found_404.html")


def moderator(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "moderator/moderator.html", context=context)


def delete_user(request):
    path = request.GET.get("next")

    user_search = User.objects.get(id=request.GET.get("user_id"))
    user_search.delete()

    return redirect(path)


def add_menejer(request, pk):
    profile_user = User.objects.get(id=pk)
    profile_user.is_staff = True
    profile_user.save()

    return redirect("moderator_main")


def delete_menejer(request, pk):
    user = User.objects.get(id=pk)
    user.is_staff = False
    user.save()

    return redirect("moderator_main")


class edit(UpdateView):
    model = Product
    template_name = "moderator/edit_cart.html"

    form_class = EditForm


class create(CreateView):
    model = Product
    template_name = "moderator/edit_cart.html"

    form_class = EditForm


def delete(request, pk):
    b = Product.objects.filter(pk=pk)
    path = request.path
    b.delete()

    return redirect("moderator_main")


def manager_main(request):
    if request.user.is_staff:
        if request.method == "POST":
            id = request.GET.get("order_id")
            order = Order.objects.get(pk=id)
            order.status = request.POST.get("status")
            order.save()
    else:
        return render(request, "found_404.html")

    orders = Order.objects.all()
    products = ProductInOrder.objects.all()
    context = {"orders": reversed(orders), "products": products}
    return render(request, "moderator/index.html", context=context)


def comment(request):
    comments = CommentsProduct.objects.all().order_by("-id")
    context = {
        "comments": comments,
    }
    return render(request, "moderator/comment_moderator.html", context=context)


def delete_comment(request):
    if request.method == "POST":
        comment_id = request.GET.get("comment_id")
        find_comment = CommentsProduct.objects.get(id=comment_id)
        find_comment.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def public_comment(request):
    if request.method == "POST":
        comment_id = request.GET.get("comment_id")
        find_comment = CommentsProduct.objects.get(id=comment_id)
        find_comment.is_publishe = True
        find_comment.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
