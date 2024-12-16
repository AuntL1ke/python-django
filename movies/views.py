from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie



def list(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def details(request, id):
    movie = Movie.objects.get(id=id)
    # TODO: check if user exists

    return render(request, "details.html", {"movie": movie})