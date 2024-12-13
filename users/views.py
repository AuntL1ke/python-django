from django.http import HttpResponse
from django.shortcuts import render


movies = [
    {
        "id": 1,
        "name": "Тачки",
        "year":2006
    },
    {
        "id": 2,
        "name": "Тачки 2",
        "year":2011
    },
    {
        "id": 3,
        "name": "Тачки 3",
        "year":2016
    },
]


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello from Django!</h1>")


def list(request):

    html = "<h1>Users</h1>"
    html += "<ul>"
    for movie in movies:
        html += f"<li>{movie['name']} --- {movie['year']}</li>"
    html += "</ul>"

    return HttpResponse(html)


def details(request, id):
   
    movie = [movie for movie in movies if movie['id'] == id]
    

    if movie:
     
        movie = movie[0]
        return HttpResponse(f"<h1>Movie Details:</h1><p>ID: {movie['id']}</p><p>Name: {movie['name']}</p><p>Year: {movie['year']}</p>")
    else:
     
        return HttpResponse("<h1>Movie not found</h1>", status=404)



def about(request):
    return HttpResponse("<h1>About Page!</h1>")