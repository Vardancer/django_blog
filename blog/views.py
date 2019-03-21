from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article, Comment

# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'

