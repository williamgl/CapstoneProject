from django.urls import path
from quiz import views

# define the urls
urlpatterns = [
    path('latest-questions/', views.LatestQuestionsList.as_view()),
    path('questions/<slug:category_slug>/<slug:product_slug>/', views.QuestionDetail.as_view()),
    path('questions/<slug:category_slug>/', views.TaskDetail.as_view()),
]
