from django.shortcuts import get_object_or_404, redirect, render
from movies.models import Movie

def list(request):
 
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})


def details(request, id):

    movie = get_object_or_404(Movie, id=id)
    return render(request, "details.html", {"movie": movie})


def delete(request, id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return redirect("list") 
    return redirect("list")
