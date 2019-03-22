from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Article, Comment
from blog.forms import AddCommentForm

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.kwargs['pk'])

        return context


class AddComment(CreateView):
    form_class = AddCommentForm


