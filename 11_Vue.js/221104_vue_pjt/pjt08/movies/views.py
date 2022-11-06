from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre

# Create your views here.
def index(request):
    movies = get_list_or_404(Movie)
    genres = Genre.movie_set
    context = {
        'movies' : movies,
        'genres' : genres,
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)