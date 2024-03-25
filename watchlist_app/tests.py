from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name = "Netflix", description = "#1 Platform",
                                                           website = "www.netflix.com")
        
        
    def test_streamplatform_create(self):
        data = {
            "name" : "netflix",
            "about" : "#1 Streaming platform",
            "website" : "http://netflix.com"
        }
        
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args = (self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name = "Netflix", description = "#1 Platform",
                                                           website = "www.netflix.com")
        
        self.watchlist = models.WatchList.objects.create(platform= self.stream, title = "Example",
                                                         storyline = "Example storyline", active = True)
    
    def test_watchlist_create(self):
        data = {
            "title" : "Example movie",
            "storyline" : "Example story",
            "platform" : self.stream,
            "active" : True    
        }
        
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(),1)
        self.assertEqual(models.WatchList.objects.get(id=1).storyline,'Example storyline')