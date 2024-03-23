
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (ReviewDetail, ReviewList, UserReview, WatchListAV, ReviewCreate, WatchDetailAV, 
                                     StreamPlatformAV, StreamPlatformDetailAV, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename = 'streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    
    path('',include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('review/', UserReview.as_view(), name='user-review-detail'),

    
]
