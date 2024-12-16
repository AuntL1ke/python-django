from django.http import HttpResponse
from django.shortcuts import render

from users.models import User


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def list(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})


def details(request, id):
    user = User.objects.get(id=id)
    # TODO: check if user exists

    return render(request, "details.html", {"user": user})