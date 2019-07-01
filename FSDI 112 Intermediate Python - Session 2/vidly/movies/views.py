from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Genre

# Create your views here.

def index(request):
    # Movie.objects.all() read all the tables
    # Moview.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)
    catalog = Movie.objects.all()
    return render(request, 'views/index.html',{'catalog': catalog,'title': 'This is the page title'})

# /movied/detail/1
# find the object with id = 1
def detail(request, movie_id):
    #return HttpResponse ("I'm a detail page" + str(movie_id))
    the_movie = Movie.objects.get(id=movie_id)
    return render(request, 'views/detail.html', {'movie': the_movie})

def test(request):
    return HttpResponse("<h1>I'm a test</h1>")

def contact(request):
    return HttpResponse("<h1>Page under construction</h1>")