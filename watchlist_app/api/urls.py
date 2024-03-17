
from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (ReviewDetail, ReviewList, WatchListAV, MovieDetail, 
                                     StreamPlatformAV, StreamDetail)



urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamDetail.as_view(), name='streamplatform-detail'),
    
    path('stream/<int:pk>/review', StreamDetail.as_view(), name='streamplatform-detail'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('review/', ReviewList.as_view(), name='review-list'),
    
]
