from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, team=self.team)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.workout = Workout.objects.create(name='Hero HIIT', description='High intensity', suggested_for='Marvel')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
