from django.shortcuts import get_object_or_404, redirect, render
from movies.models import Movie
from movies.forms import CreateMovie, EditMovie
def list(request):
 
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

def edit(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return redirect("/movies/list")

    form = EditMovie(instance=movie)

    if request.method == "POST":
        form = EditMovie(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect("/movies/list")

    return render(request, "edit.html", {"form": form})

def details(request, id):

    movie = get_object_or_404(Movie, id=id)
    return render(request, "details.html", {"movie": movie})

def create(request):
    form = CreateMovie()

  
    if request.method == "POST":
        form = CreateMovie(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/movies/list")

    return render(request, "create.html", {"form": form})

# def delete(request, id):
#     if request.method == "POST":
#         movie = get_object_or_404(Movie, id=id)
#         movie.delete()
#         return redirect("list") 
#     return redirect("list")

def delete(request, id):
    movie = Movie.objects.get(id=id)

    if movie is not None:
        movie.delete()

    return redirect("/movies/list")