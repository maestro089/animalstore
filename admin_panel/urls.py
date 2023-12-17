from django.urls import path

from admin_panel import views

urlpatterns = [
    path("", views.moderator_main, name="moderator_main"),
    path("moderator/", views.moderator, name="moderator"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("add_menejer/<int:pk>", views.add_menejer, name="add_menejer"),
    path("edit_book/<int:pk>", views.edit.as_view(), name="edit"),
    path("create_book/", views.create.as_view(), name="create"),
    path("delete_book/<int:pk>", views.delete, name="delete"),
    path("delete_menejer/<int:pk>", views.delete_menejer, name="delete_menejer"),
    path("manager", views.manager_main, name="manager_main"),
    path("comments", views.comment, name="comment_moderator"),
    path("delete_comment", views.delete_comment, name="delete_comment"),
    path("public_comment", views.public_comment, name="public_comment"),
]
