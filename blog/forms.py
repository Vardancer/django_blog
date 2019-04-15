from django.forms import models
from django.forms.widgets import CheckboxInput
from blog.models import Article, Comment, Answers, Questions, Survey


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
        model = Questions
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey')
        self.survey = survey
        super(SurveyAnswer, self).__init__(*args, **kwargs)


# https://github.com/jessykate/django-survey/tree/master/survey
# https://github.com/bitlabstudio/django-multilingual-survey/tree/master/multilingual_survey
# https://github.com/seantis/seantis-questionnaire/blob/master/questionnaire/models.py


