from django.urls import path
from blog.views import ArticleListView, ArticleDetailView, AddArticle, SurveyView


urlpatterns = [
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('article/create/', AddArticle.as_view(), name='article_create'),
    path('survey/<int:pk>/', SurveyView.as_view(), name='surv-det'),
    path('', ArticleListView.as_view(), name='article-list'),
]

