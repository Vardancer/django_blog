from django.forms import models
from django.forms.widgets import CheckboxInput
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
        widgets = {
            'is_checked': CheckboxInput(attrs={'required': 'False'})
        }


# https://github.com/jessykate/django-survey/tree/master/survey
# https://github.com/bitlabstudio/django-multilingual-survey/tree/master/multilingual_survey
# https://github.com/seantis/seantis-questionnaire/blob/master/questionnaire/models.py


