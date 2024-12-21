from django.urls import path
from movies import views

urlpatterns = [
    path("list/", views.list, ),
    path("create/", views.create),
    path("details/<int:id>", views.details,),
    path("delete/<int:id>", views.delete,),
    path("edit/<int:id>", views.edit),
]
