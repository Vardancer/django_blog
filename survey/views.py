from django.views.generic import FormView
from survey.models import Survey, User, Response, Answers, Questions
from survey.forms.survey_form import SurveyForm
from django.urls import reverse_lazy
from django.http import Http404


class SurveyView(FormView):
    form_class = SurveyForm
    template_name = 'survey_form.html'
    success_url = reverse_lazy('article-list')

    def dispatch(self, request, *args, **kwargs):
        try:
            self.survey = Survey.objects.get(pk=kwargs['survey'])
        except Survey.DoesNotExist:
            raise Http404
        return super(SurveyView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'survey': self.survey})
        return context

    def get_form_kwargs(self):
        kwargs = super(SurveyView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'survey': self.survey,
        })
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        context = self.get_context_data(form=form)
        context.update({'success': True})
        return self.render_to_response(context)
