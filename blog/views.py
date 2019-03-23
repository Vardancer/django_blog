# from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from blog.models import Article, Comment
from blog.forms import AddCommentForm, CreateArticleForm

# Create your views here.


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

