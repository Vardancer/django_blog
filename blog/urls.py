from django.urls import path
from blog.views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
]

