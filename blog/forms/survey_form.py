from django.forms import Form, CheckboxSelectMultiple, MultipleChoiceField
from blog.models import Survey, Questions, Answers, User


class SurveyForm(Form):
    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        surv_id = kwargs['initial'].pop('survey')
        quest = Questions.objects.filter(survey=surv_id)

        for q in quest:
            q_choices = q.get_choices()
            self.fields["question_%d" % q.pk] = MultipleChoiceField(label=q.question,
                                                                    widget=CheckboxSelectMultiple,
                                                                    choices=q_choices)

    # @staticmethod
    def save(self, survey):

        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith("question_"):
                q_id = int(field_name.split("_")[1])
                print(q_id, field_value)


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
