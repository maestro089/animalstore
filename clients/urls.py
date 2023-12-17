from django.urls import path

from clients import views

urlpatterns = [
    path("login/", views.log_in, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("logup/", views.log_up, name="logup"),
]
