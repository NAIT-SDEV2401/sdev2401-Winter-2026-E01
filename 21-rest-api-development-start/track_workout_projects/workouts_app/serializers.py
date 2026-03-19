from rest_framework import serializers
from .models import Exercise, Workout, WorkoutLog

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.CharField(max_length=50)