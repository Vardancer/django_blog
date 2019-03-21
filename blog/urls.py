from django.urls import path
from blog.views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
]