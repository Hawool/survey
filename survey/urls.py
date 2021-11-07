from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('surveys/', views.SurveyListViewSet.as_view()),  #
    path('survey/create', views.SurveyCreateViewSet.as_view({'post': 'create'})),  #
    path('survey/current', views.SurveyCurrentViewSet.as_view()),  #
    path('survey/<int:pk>/', views.SurveyDetailViewSet.as_view()),  #
    path('survey/<int:pk>/update', views.SurveyDetailUpdateViewSet.as_view()),  #
    path('survey/<int:pk>/delete', views.SurveyDetailDestroyViewSet.as_view()),  #

    path('question/', views.QuestionListViewSet.as_view()),
    path('question/create', views.QuestionCreateViewSet.as_view()),
    path('question/<int:pk>/update/', views.QuestionUpdateViewSet.as_view()),
    path('question/<int:pk>/delete/', views.QuestionDestroyViewSet.as_view()),

    path('answer/all', views.AnswerListViewSet.as_view()),  #
    path('user_answers/', views.AnswerUserListCreateViewSet.as_view()),  #
]

urlpatterns = format_suffix_patterns(urlpatterns)
