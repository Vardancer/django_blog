from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, help_text="Title")
    text = models.TextField(help_text="A blog body")
    date_add = models.DateField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET(0))
    comment = models.CharField(max_length=200, default=None)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -- {}".format(self.comment[:50], self.user)

