from django.db.models import Q
from django.shortcuts import render

from filmy.models import Movie, Genre, Actor, Director


def movies(request):
    movies_queryset = Movie.objects.all().order_by('name')
    genre = request.GET.get('genre')
    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)
    search = request.GET.get('search')
    if search:
        movies_queryset = movies_queryset.filter(Q(name__icontains=search)|Q(description__icontains=search)) 

    context = {
        "movies": movies_queryset,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
        "search": search,
    }
    return render(request, 'filmy/movies.html', context)


def movie(request, id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    return render(request, 'filmy/movie.html', context)


def actors(request):
    context = {
        'actors': Actor.objects.all().order_by('name')
    }

    return render(request, 'filmy/actors.html', context)


def actor(request, id):
    context = {
        'actor': Actor.objects.get(id=id)
    }

    return render(request, 'filmy/actor.html', context)


def director(request, id):
    context = {
        'director': Director.objects.get(id=id)
    }

    return render(request, 'filmy/director.html', context)


def directors(request):
    context = {
        'directors': Director.objects.all().order_by('name')
    }

    return render(request, 'filmy/directors.html', context)