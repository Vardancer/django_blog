from collections import OrderedDict
from django.forms.utils import ErrorList
from django.forms import Form, CheckboxSelectMultiple, MultipleChoiceField
from django.forms import ModelMultipleChoiceField, ModelChoiceField
from django.forms import ChoiceField, RadioSelect
from survey.models import Survey, Questions, Answers, User, Response
import uuid


class SurveyForm(Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.survey = kwargs.pop('survey', None)
        super(SurveyForm, self).__init__(*args, **kwargs)
        # choices = []
        for question in self.survey.questions.all():
            queryset = question.answers.all()
            req = question.required
            if queryset:
                field_kwargs = {
                    'label': question,
                    'queryset': queryset,
                    'required': False,
                    # 'widget': RadioSelect,
                }
                print(field_kwargs, req)
                if question.is_multiselect:
                    field_kwargs.update({
                        'widget': CheckboxSelectMultiple,
                    })
                    self.fields.update({
                        question.answers: ModelMultipleChoiceField(**field_kwargs)
                    })
                else:
                    field_kwargs.update({
                        'widget': RadioSelect(attrs={'class': 'special'}),
                        'empty_label': None,
                    })
                    self.fields.update({
                        question.answers: ModelChoiceField(**field_kwargs),
                    })

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
        # pass
        for question in self.survey.questions.all():
            # response = self.cleaned_data
            print(self.cleaned_data)
            # if self.user:
            #     resp_obj, crtd = Response.objects.get_or_create(
            #         user=self.user, question=question, survey=self.survey
            #     )
            # print(resp_obj, crtd)
            # resp_obj.answer.clear()

            # if response:
            #     if isinstance(response, Answers):
            #         resp_obj.answer.add(response)
            #     else:
            #         for answer in response:
            #             resp_obj.answer.add(answer)

            # resp_obj.save()
        return self.survey


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
