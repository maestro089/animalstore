from django.urls import path

from news import views

urlpatterns = [
    path("", views.get, name="news"),
    path("<int:pk>/", views.get_info, name="new_info"),
    path("create/", views.create, name="new_create"),

]
