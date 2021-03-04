from django.urls import path
from moviesinfo import views

urlpatterns = [
    path('', views.index_view),
    path('addmovie/', views.add_movie_view),
    path('listmovies/', views.list_movie_view),
]
