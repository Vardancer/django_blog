from django.forms import models
from blog.models import Article, Comment, Answers


class AddCommentForm(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CreateArticleForm(models.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'active']


class SurveyAnswer(models.ModelForm):
    class Meta:
        model = Answers
        fields = ('question', 'is_checked')


