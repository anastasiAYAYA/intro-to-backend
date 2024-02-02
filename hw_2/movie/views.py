from django.shortcuts import render
from .models import Movie


def get_index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies': movies})


def get_info(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie/movie_info.html', {'movie': movie})
