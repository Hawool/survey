from rest_framework.serializers import ModelSerializer

from .models import Survey, Question, Answer


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'end_date', 'start_date', 'description']
        extra_kwargs = {
            'start_date': {'read_only': True}
        }


class QuestionSerializer(ModelSerializer):
    survey = SurveySerializer

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    """Список ответов"""
    survey = SurveySerializer
    question = QuestionSerializer

    class Meta:
        model = Answer
        fields = '__all__'
