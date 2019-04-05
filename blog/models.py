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


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(0))
    comment = models.CharField(max_length=200, default=None)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -- {}".format(self.article.title, self.date_add)


class Category(models.Model):
    name = models.CharField(max_length=200)


class Survey(models.Model):
    description = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)
    need_logged_user = models.BooleanField(default=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("survey-detail", kwargs={"id": self.pk})


class Questions(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        unique_together = ("question", "survey")

    def __str__(self):
        return self.question



