from django.contrib import admin
from filmy.models import Movie

class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)