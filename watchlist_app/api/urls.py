
from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import MovieListAV, MovieDetail


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-details'),
]
