from django.contrib import admin
from moviesinfo.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['ryear','moviename','hero','heroine', 'rating']

admin.site.register(Movie, MovieAdmin)
