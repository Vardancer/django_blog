from django.forms import Form, CheckboxSelectMultiple, MultipleChoiceField, ModelMultipleChoiceField, ModelChoiceField
from django.forms import ChoiceField, RadioSelect
from survey.models import Survey, Questions, Answers, User, Response
import uuid


class SurveyForm(Form):
    def __init__(self, user, survey, data=None, initial=None):

        self.user = user if user.is_authenticated() else None
        self.survey = survey
        self.base_fields = {}
        self.is_bound = data is not None

        self.data = data or {}

        self.initial = initial or self.get_initial()

        for question in self.survey.objects.all():
            queryset = question.answers.all()

            if queryset:
                field_kwargs = {
                    'label': question,
                    'queryset': queryset,
                    'required': False,
                }

                if question.is_multiselect:
                    field_kwargs.update({
                        'widget': CheckboxSelectMultiple,
                    })
                    self.fields.update({
                        question.answers: ModelMultipleChoiceField(**field_kwargs)
                    })
                else:
                    self.fields.update({question.answers: ModelChoiceField(**field_kwargs)})

    def get_initial(self):
        initial = {}

        for question in self.survey.questions.all():
            if self.user:
                try:
                    response = self.user.responses.filter(
                        question=question).distinct().get()
                except Response.DoesNotExist:
                    continue




# class SurveyAnswerForm(models.ModelForm):
#
#     class Meta:
#         model = Answers
#         fields = ['user']
#
#     def __init__(self, *args, **kwargs):
#         super(SurveyAnswerForm, self).__init__(*args, **kwargs)
#
#         # data = kwargs.get('data')
#         survey_id = kwargs['initial'].pop('survey')
#         quest = Questions.objects.filter(survey=survey_id)
#         for q in quest:
#             q_choices = q.get_choices()
#             self.fields["question_%d" % q.pk] = forms.MultipleChoiceField(label=q.question,
#                                                                           widget=forms.CheckboxSelectMultiple,
#                                                                           choices=q_choices)


# https://github.com/jessykate/django-survey/tree/master/survey
# https://github.com/bitlabstudio/django-multilingual-survey/tree/master/multilingual_survey
# https://github.com/seantis/seantis-questionnaire/blob/master/questionnaire/models.py
