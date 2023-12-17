from django.urls import path

from cart import views

urlpatterns = [
    path("add_cart/", views.add_cart, name="add_cart"),
    path("info/", views.get, name="getcart"),
    path("delete_cart/", views.delete_cart, name="delete_cart"),
    path("order/", views.order, name="order"),
    path("place_order/", views.place_order, name="place_order"),
]
