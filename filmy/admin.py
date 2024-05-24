from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "footage", "director", "genres_display"]
    list_display_links = ["id", "name"]
    search_fields = ["=id", "name", "director__name"]
    list_filter = ["year", "genres"]
    list_editable = ["year", "footage"]

class ActorAdmin(admin.ModelAdmin):
    pass

class DirectorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)
