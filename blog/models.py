from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(0))
    title = models.CharField(max_length=100, help_text="Title")
    text = models.TextField(help_text="A blog body")
    active = models.BooleanField(verbose_name="is_published")
    date_add = models.DateField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} -- {}".format(self.title, self.author.last_name)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(0))
    comment = models.CharField(max_length=200, default=None)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -- {}".format(self.article.title, self.date_add)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


# class Category(models.Model):
#     name = models.CharField(max_length=200)


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
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey')
    question = models.CharField(max_length=255)
    choices = models.CharField(default="yes,no,maybe", max_length=200)
    required = models.BooleanField(default=False)

    def get_choices(self):
        choices = self.choices.split(',')
        c_list = []
        for c in choices:
            c = c.strip()
            c_list.append((c, c))
        choices_tuple = tuple(c_list)

        return choices_tuple

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'response'
        verbose_name_plural = 'responses'
        unique_together = ("survey", "user")

    def __str__(self):
        return "Survey subj {} done by {}".format(self.survey.title, self.user.username)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    answer = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'



