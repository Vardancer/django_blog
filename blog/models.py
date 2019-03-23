from django.contrib.auth.models import User
from django.db import models

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

