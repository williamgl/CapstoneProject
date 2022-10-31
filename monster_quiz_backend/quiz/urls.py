from django.urls import path
from quiz import views

# define the urls
urlpatterns = [
    path('latest-questions/', views.LatestQuestionsList.as_view()),
    path('questions/<slug:quiz_slug>/<slug:question_slug>/', views.QuestionDetail.as_view()),
    path('questions/<slug:quiz_slug>/', views.QuizDetail.as_view()),
]
