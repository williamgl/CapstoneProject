from rest_framework import serializers
from .models import Quiz, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "score",
        )


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "completed",
            "questions",
        )
