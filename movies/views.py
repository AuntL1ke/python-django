from django.shortcuts import get_object_or_404, redirect, render
from django.forms import model_to_dict
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
        form = EditMovie(request.POST, request.FILES, instance=movie)

        if len(request.FILES) > 0 and user.avatar:
                user.avatar.delete()
        if form.is_valid():
            form.save()
            return redirect("/movies/list")

    return render(request, "edit.html", {"form": form, "positions": Movie.POSITIONS, "return_url": "/movies/list"})

    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return redirect("/movies/list")

    form = EditMovie(instance=movie)

    if request.method == "POST":
        form = EditMovie(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/movies/list")
    if user.avatar:
        user.avatar.delete()
    return render(request, "edit.html", {"form": form})

def details(request, id):

    movie = get_object_or_404(Movie, id=id)
    
    # print(movie.avatar)
    # print(movie.avatar.url)
    
    return render(request, "details.html", {
        "movie": {
            **model_to_dict(movie),
            "positionName": dict(movie.POSITIONS).get(movie.position)
        }, 
        "return_url": "/movies/list"
    })

def create(request):
    form = CreateMovie()

  
    if request.method == "POST":
        form = CreateMovie(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/movies/list")

    return render(request, "create.html", {"form": form, "positions": Movie.POSITIONS, "return_url": "/movies/lisr"})


# def delete(request, id):
#     if request.method == "POST":
#         movie = get_object_or_404(Movie, id=id)
#         movie.delete()
#         return redirect("list") 
#     return redirect("list")

def catalog(request):
    movies = Movie.objects.all()
    return render(request, "catalog.html", {"movies": movies})

def delete(request, id):
    movie = Movie.objects.get(id=id)

    if movie is not None:
        movie.delete()

    return redirect("/movies/list")