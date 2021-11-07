from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Survey(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='question_survey', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    TEXT = 'TEXT'
    ONE_ANSWER = 'ONE_ANSWER'
    MULTI_ANSWER = 'MULTI_ANSWER'
    TYPE = [
        (TEXT, 'Ответ текстом'),
        (ONE_ANSWER, 'Ответ с выбором одного варианта'),
        (MULTI_ANSWER, 'Ответ с выбором нескольких вариантов'),
    ]
    type = models.CharField(
        verbose_name="Тип вопроса",
        max_length=100,
        choices=TYPE,
        default=TEXT,
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class Answer(models.Model):
    owner = models.ForeignKey(User, related_name='answer_owner', on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name='answer_survey', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answer_question', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.text

