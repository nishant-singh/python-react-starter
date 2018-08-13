from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^quiz/', include('play.urls')),
    url(r'^lead/', TemplateView.as_view(template_name='lead.html')),
]


"""
url(r'^get_quiz?userid=<int:userid>/',),
url(r'^quiz/', include('play.urls')),
TemplateView.as_view(template_name='quiz.html'),
"""
