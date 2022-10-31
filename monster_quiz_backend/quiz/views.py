from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .serializers import QuizSerializer, QuestionSerializer
from .models import Quiz, Question


# Create your views here.
class LatestQuestionsList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()[0:4]
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionDetail(APIView):
    def get_object(self, quiz_slug, question_slug):
        try:
            return Question.objects.filter(quiz__slug=quiz_slug).get(slug=question_slug)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, quiz_slug, question_slug, format=None):
        question = self.get_object(quiz_slug, question_slug)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class TaskDetail(APIView):
    def get_object(self, quiz_slug):
        try:
            return Quiz.objects.get(slug=quiz_slug)
        except Quiz.DoesNotExist:
            raise Http404

    def get(self, request, quiz_slug, format=None):
        task = self.get_object(quiz_slug)
        serializer = QuizSerializer(task)
        return Response(serializer.data)
