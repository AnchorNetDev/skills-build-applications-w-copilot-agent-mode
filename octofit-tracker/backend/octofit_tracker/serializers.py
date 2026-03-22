from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    team = TeamSerializer()
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'team']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']
