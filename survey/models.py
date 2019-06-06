from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Survey(models.Model):
    title = models.CharField(max_length=50, default="test")
    description = models.CharField(max_length=150)
    # is_published = models.BooleanField(default=False)
    # need_logged_user = models.BooleanField(default=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("survey-detail", kwargs={"id": self.pk})

    class Meta:
        verbose_name = 'survey'
        verbose_name_plural = 'surveys'


class Questions(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=256, blank=True)
    required = models.BooleanField(default=False)
    answers = models.ManyToManyField('Answers', related_name='answers')
    is_multiselect = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    question = models.ForeignKey(Questions, verbose_name='Question', related_name='responses', on_delete=models.CASCADE)
    answer = models.ManyToManyField('Answers', verbose_name='Answer', related_name='responses')

    def __str__(self):
        return "Survey subj {} done by {}".format(self.survey.title, self.user.username)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='questions')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


