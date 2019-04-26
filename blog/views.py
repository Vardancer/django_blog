from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.views.generic.edit import FormMixin, ModelFormMixin
from blog.models import Article, Comment, Survey, Questions, Answers
from blog.forms.cbv_forms import AddCommentForm, CreateArticleForm
from blog.forms.survey_form import SurveyForm


# Create your views here.
# TODO https://github.com/django-ckeditor/django-ckeditor
# todo make beauty with bootstrap4, https://getbootstrap.com/docs/4.3/content/typography/


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'article-detail.html'
    context_object_name = 'article'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse('article', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.kwargs['pk'])
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comm = form.save(commit=False)
        comm.user = self.request.user
        comm.article = self.object
        comm.save()
        return super(ArticleDetailView, self).form_valid(form)


class AddArticle(CreateView):
    form_class = CreateArticleForm
    success_url = reverse_lazy('article-list')
    template_name = 'article_create.html'


class SurveyView(FormView):
    form_class = SurveyForm
    template_name = 'survey.html'
    success_url = reverse_lazy('article-list')

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            "survey": self.kwargs['survey']
        })
        return initial

    def form_valid(self, form):
        user: int = self.request.user
        form.save(survey=self.kwargs['survey'], user=user)
        return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['survey'] = kwargs.get('pk')
    #     return context




