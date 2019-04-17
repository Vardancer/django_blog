from django.forms import models
from blog.models import Article, Comment


class AddCommentForm(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CreateArticleForm(models.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'active']


