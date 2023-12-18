from django.urls import path

from store import views

urlpatterns = [
    path("/store", views.get, name="store"),
    path("<int:pk>", views.info, name="product"),
    path("", views.main, name="home"),
    path("about", views.about, name="about"),
]
