from django.conf.urls import url, include
from django.views.generic import *
from . import views


urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.index.as_view(), name='home'),
]
