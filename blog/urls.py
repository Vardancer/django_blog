from django.urls import path
from blog.views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<int:id>/', ArticleDetailView.as_view(), name='article'),
]

