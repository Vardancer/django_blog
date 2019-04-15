from django.forms import models
from django import forms
from blog.models import Article, Comment, Answers, Questions, Survey


class AddCommentForm(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CreateArticleForm(models.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'active']


class SurveyAnswerForm(models.ModelForm):

    class Meta:
        model = Questions
        fields = ('question',)

    def __init__(self, *args, **kwargs):
        super(SurveyAnswerForm, self).__init__(*args, **kwargs)

        # data = kwargs.get('data')

        for q in Survey.objects.filter(kwargs.get('pk')):
            q_choices = q.get_choices()
            self.fields["question_%d" % q.pk] = forms.MultipleChoiceField(label=q.question,
                                                                          widget=forms.CheckboxSelectMultiple,
                                                                          choices=q_choices)


# https://github.com/jessykate/django-survey/tree/master/survey
# https://github.com/bitlabstudio/django-multilingual-survey/tree/master/multilingual_survey
# https://github.com/seantis/seantis-questionnaire/blob/master/questionnaire/models.py


