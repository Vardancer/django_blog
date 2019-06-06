from django.urls import path
from survey.views import SurveyView


urlpatterns = [
    path('<int:survey>/', SurveyView.as_view(), name='surv-det'),
    ]

