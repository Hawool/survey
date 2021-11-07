from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Survey, Question, Answer
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
import datetime


class SurveyListViewSet(generics.ListAPIView):
    """Get list of survey"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyCreateViewSet(ModelViewSet):
    """Create survey"""
    # queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAdminUser]


class SurveyCurrentViewSet(generics.ListAPIView):
    """Get current surveys"""
    queryset = Survey.objects.filter(end_date__gte=datetime.datetime.now())
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyDetailViewSet(generics.RetrieveAPIView):
    """Get one survey"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]


class SurveyDetailUpdateViewSet(generics.UpdateAPIView):
    """Update question"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAdminUser]


class SurveyDetailDestroyViewSet(generics.DestroyAPIView):
    """Destroy question"""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionListViewSet(generics.ListAPIView):
    """Get list of question"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionCreateViewSet(generics.CreateAPIView):
    """Create question"""
    # queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionUpdateViewSet(generics.UpdateAPIView):
    """Update question"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionDestroyViewSet(generics.DestroyAPIView):
    """Destroy question"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListViewSet(generics.ListAPIView):
    """Get list of answer and create"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerUserListCreateViewSet(APIView):
    """Get User's answer's"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = Answer.objects.filter(owner=self.request.user)
        serializer = AnswerSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

