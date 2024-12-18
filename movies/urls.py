from django.urls import path
from movies import views

urlpatterns = [
    path("list/", views.list, name="list"),
    path("details/<int:id>", views.details, name="details"),
    path("delete/<int:id>", views.delete, name="delete"),
]
