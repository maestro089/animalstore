from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView

from store.models import Product, CommentsProduct



from news.models import News
def main(request):
    news = News.objects.filter().order_by("-id")[0:3]
    context = {"news": news}
    return render(request, "main.html", context)

def get(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "store/index.html", context)


def info(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        text = request.POST.get("Text")
        for word in text.lower().split():
            CommentsProduct.objects.create(
                is_publishe=False,
                author=request.user,
                text=request.POST.get("Text"),
                comment_product=product,
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        CommentsProduct.objects.create(
            author=request.user, text=text, comment_product=product
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    comments = CommentsProduct.objects.filter(comment_product=product)

    context = {
        "product": product,
        "comments": comments,
    }

    return render(request, "store/product.html", context)
