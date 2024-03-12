
from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import WatchListAV, MovieDetail, StreamPlatformAV, StreamDetail


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamDetail.as_view(), name='stream-details'),
]
