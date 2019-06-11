from collections import OrderedDict
from django.forms.utils import ErrorList
from django.forms import Form, CheckboxSelectMultiple, MultipleChoiceField
from django.forms import ChoiceField, RadioSelect
from survey.models import Survey, Questions, Answers, User, Response
import uuid


class SurveyForm(Form):
    def __init__(self, user, survey, data=None, initial=None, prefix=None,
                 auto_id='id_%s', empty_permitted=False, error_class=ErrorList, label_suffix=':'):

        self.user = user if user.is_authenticated else None
        self.survey = survey
        self.base_fields = {}
        self.label_suffix = label_suffix
        self.prefix = prefix
        self.is_bound = data is not None
        self.error_class = error_class
        self.data = data or {}
        self.auto_id = auto_id
        self.fields = OrderedDict()
        self.initial = initial or self.get_initial()
        self._errors = None
        self._changed_data = None
        self._bound_fields_cache = {}
        # choices = []
        for question in self.survey.questions.all():
            choices = [a.answer for a in question.answers.all()]

            if choices:
                field_kwargs = {
                    'label': question,
                    'choices': choices,
                    'required': False,
                }
                print(field_kwargs)
                if question.is_multiselect:
                    field_kwargs.update({
                        'widget': CheckboxSelectMultiple,
                    })
                    self.fields.update({
                        question.answers: MultipleChoiceField(**field_kwargs)
                    })
                else:
                    self.fields.update({question.answers: ChoiceField(**field_kwargs)})

    def get_initial(self):
        initial = {}

        for question in self.survey.questions.all():
            if self.user:
                try:
                    response = self.user.user.filter(
                        question=question).distinct().get()
                except Response.DoesNotExist:
                    continue
            else:
                try:
                    response = Response.objects.filter()
                except Response.DoesNotExist:
                    continue

            if question.is_multiselect:
                initial[question] = [resp.pk for resp in response.answer.all()]
            elif response.answer.all():
                initial[question] = response.answer.all()[0].pk
        return initial

    def clean(self):
        for question in self.survey.questions.all():
            if question.required:
                response = self.cleaned_data.get(question)
                if not response:
                    self._errors = ['Some error']
        return self.cleaned_data

    def save(self):
        pass


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
