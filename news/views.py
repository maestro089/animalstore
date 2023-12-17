from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView

from news.models import News, Comment


def get(request):
    news = News.objects.all()

    return render(request, "news/index.html", context={"news": news})


def get_info(request, pk):
    news = News.objects.get(pk=pk)
    comments = Comment.objects.filter(news_id=pk)

    if request.method == "POST":
        Comment.objects.create(
            author=request.user, text=request.POST.get("Text"), news_id=news
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return render(request, "news/news.html", context={"new": news, "comment": comments})


def create(request):
    if request.method == "POST":
        News.objects.create(
            title=request.POST.get("title"),
            photo=request.POST.get("photo"),
            text=request.POST.get("text"),
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def main(request):
    news = News.objects.filter().order_by("-id")[0:3]
    context = {"news": news}
    return render(request, "main.html", context)
