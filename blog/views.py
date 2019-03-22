# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from blog.models import Article, Comment
from blog.forms import AddCommentForm

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'


class ArticleDetailView(DetailView, FormMixin):
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

    @login_required
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

# class AddComment(CreateView):
#     form_class = AddCommentForm


