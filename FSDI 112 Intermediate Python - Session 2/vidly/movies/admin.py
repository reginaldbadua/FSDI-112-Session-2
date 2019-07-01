from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')# tuple

class MovieAdmin(admin.ModelAdmin):
    # exclude = ('price',)
    # fields = ('title', 'stock') # List what properties the user will capture
    list_display = ('id', 'title', 'stock', 'price')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
