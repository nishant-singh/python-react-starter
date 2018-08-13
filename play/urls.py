from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # /quiz/
    url(r'^$', TemplateView.as_view(template_name='quiz.html')),
    #url(r'^abcd/', views.quesList.as_view())
    url(r'^(?P<user_id>[-\w]+)$', views.quesList.as_view(), 'domain.views.output')
]