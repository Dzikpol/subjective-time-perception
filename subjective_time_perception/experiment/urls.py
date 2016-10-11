from django.conf.urls import url
from django.views.generic import TemplateView
from subjective_time_perception.experiment.views import ExperimentCreateView
from subjective_time_perception.experiment.views import ExperimentResultCsvView
from subjective_time_perception.experiment.views import ExperimentResultHtmlView


urlpatterns = [
    url(r'experiment/api/$', ExperimentCreateView.as_view()),
    url(r'experiment/result.csv$', ExperimentResultCsvView.as_view()),
    url(r'experiment/result.html$', ExperimentResultHtmlView.as_view()),
]
